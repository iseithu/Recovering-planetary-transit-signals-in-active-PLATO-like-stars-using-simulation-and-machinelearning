import numpy as np
import os

# =====================
# SETTINGS
# =====================
N = 250
output_dir = "generated_yaml_class_2"
os.makedirs(output_dir, exist_ok=True)

np.random.seed(42)

# =====================
# PARAMETER RANGES (CLASS 2: PLANET + MEDIUM ACTIVITY)
# =====================

# ID
ids = np.arange(30000, 30000 + N)

# Stellar
mag = np.random.uniform(9, 12, N)
rotation = np.random.uniform(5, 30, N)
inclination = np.random.uniform(60, 90, N)

# Flare (MEDIUM)
flare_period = np.random.uniform(2, 5, N)
flare_amp = np.random.uniform(1000, 2000, N)

# Planet
radius = np.random.uniform(0.8, 4, N)
orbital_period = np.random.uniform(2, 50, N)
impact = np.random.uniform(0, 0.8, N)

# Seed
seed = np.random.randint(1, 1000000000, N)

# =====================
# LOAD TEMPLATE
# =====================
with open("templateclass2.yaml", "r") as f:
    template = f.read()

# =====================
# GENERATE YAML FILES
# =====================
for i in range(N):

    content = template.format(
        id=int(ids[i]),
        mag=round(mag[i], 3),
        rotation=round(rotation[i], 3),
        inclination=round(inclination[i], 3),

        flare_period=round(flare_period[i], 3),
        flare_amp=round(flare_amp[i], 3),

        radius=round(radius[i], 3),
        period=round(orbital_period[i], 3),
        impact=round(impact[i], 3),

        seed=int(seed[i]),

        #  IMPORTANT (PySpot)
        external_file="/home/israt/Downloads/psls/fixed_lc.txt"
    )

    filename = f"config_{i:04d}.yaml"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

print(" 250 CLASS-2 YAML files generated correctly!")
