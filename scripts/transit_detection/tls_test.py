import os
import numpy as np
import pandas as pd

from wotan import flatten
from transitleastsquares import transitleastsquares

# ====================================
# LOAD METADATA
# ====================================
metadata = pd.read_csv("metadata_v2.csv")

# ====================================
# ONLY CLASS 2 + CLASS 3
# 5 FILES EACH
# ====================================
sample_df = pd.concat([
    metadata[metadata["class"] == 2].head(15),
    metadata[metadata["class"] == 3].head(15)
])

print("Total files =", len(sample_df))

results_list = []

# ====================================
# LOOP
# ====================================
for _, row in sample_df.iterrows():

    filename = row["filename"]
    true_class = row["class"]

    print("\n================================")
    print("File :", filename)
    print("Class:", true_class)

    try:

        # -----------------------
        # Find file automatically
        # -----------------------
        filepath = None

        for root, dirs, files in os.walk("."):
            if filename in files:
                filepath = os.path.join(root, filename)
                break

        if filepath is None:
            print("File not fou
            nd")
            continue

        # -----------------------
        # Load light curve
        # -----------------------
        data = np.loadtxt(filepath)

        # SPEED UP
        data = data[::20]

        time = data[:,0] / 86400.0
        flux = data[:,1]

        mask = np.isfinite(time) & np.isfinite(flux)

        time = time[mask]
        flux = flux[mask]

        flux = flux / np.mean(flux)

        print("Points =", len(time))

        # -----------------------
        # Detrend
        # -----------------------
        flat_flux, trend = flatten(
            time,
            flux,
            method="biweight",
            window_length=0.5,
            return_trend=True
        )

        # -----------------------
        # TLS
        # -----------------------
        model = transitleastsquares(
            time,
            flat_flux
        )

        tls_result = model.power(
            period_min=0.5,
            period_max=20,
            use_threads=8
        )

        sde = float(tls_result.SDE)
        period = float(tls_result.period)

        detected = sde > 7

        print("Period =", round(period,4))
        print("SDE    =", round(sde,2))
        print("Detected =", detected)

        results_list.append([
            filename,
            true_class,
            period,
            sde,
            detected
        ])

    except Exception as e:

        print("FAILED:", e)

# ====================================
# RESULTS TABLE
# ====================================
tls_df = pd.DataFrame(
    results_list,
    columns=[
        "filename",
        "class",
        "period",
        "SDE",
        "detected"
    ]
)

print("\n\n======================")
print("TLS RESULTS")
print("======================")

display(tls_df)

# ====================================
# RECOVERY FRACTION
# ====================================
print("\n======================")
print("RECOVERY FRACTION")
print("======================")

recovery = (
    tls_df.groupby("class")["detected"]
    .mean()
    * 100
)

print(recovery)

overall = tls_df["detected"].mean() * 100

print("\nOverall Recovery =", round(overall,1), "%")
