import numpy as np
import os

# =====================
# SETTINGS
# =====================
N = 250
output_dir = "generated_yaml_ class_3"
os.makedirs(output_dir, exist_ok=True)

np.random.seed(42)

# =====================
# PARAMETER RANGES (YOUR CUSTOM)
# =====================

# ID
ids = np.arange(40000, 40000 + N)

# Stellar
mag = np.random.uniform(9, 12, N)
rotation = np.random.uniform(5, 30, N)
inclination = np.random.uniform(60, 90, N)

# Activity
sigma = np.random.uniform(1200, 2000, N)
tau = np.random.uniform(5, 12, N)

# Flare
flare_period = np.random.uniform(0.5, 3, N)
flare_amp = np.random.uniform(1500, 3000, N)

# Planet
radius = np.random.uniform(0.8, 4, N)
orbital_period = np.random.uniform(2, 50, N)
impact = np.random.uniform(0, 0.8, N)

# =====================
# LOAD TEMPLATE YAML
# =====================
with open("templateclass3.yaml", "r") as f:
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
        sigma=round(sigma[i], 3),
        tau=round(tau[i], 3),
        flare_period=round(flare_period[i], 3),
        flare_amp=round(flare_amp[i], 3),
        radius=round(radius[i], 3),
        period=round(orbital_period[i], 3),
        impact=round(impact[i], 3)
    )

    filename = f"config_{i:04d}.yaml"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

print("250 YAML files generated with YOUR parameter ranges!")
