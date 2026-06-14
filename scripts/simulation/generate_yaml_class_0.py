import numpy as np
import os

# =====================
# SETTINGS
# =====================
N = 250
output_dir = "generated_yaml_class_0"
os.makedirs(output_dir, exist_ok=True)

np.random.seed(42)

# =====================
# PARAMETER RANGES (CLASS 0)
# =====================

# ID → 00000–00249
ids = np.arange(0, N)

# Stellar parameters
mag = np.random.uniform(9, 12, N)          # Krenn et al. (2024)
rotation = np.random.uniform(5, 30, N)     # McQuillan et al. (2014)

# ⚠️ Inclination Class 0 এ important না → 0–90 দিলাম (better physics)
inclination = np.random.uniform(0, 90, N)

# =====================
# LOAD TEMPLATE YAML
# =====================
with open("templateclass0.yaml", "r") as f:
    template = f.read()

# =====================
# GENERATE YAML FILES
# =====================
for i in range(N):

    content = template.format(
        id=int(ids[i]),
        mag=round(mag[i], 3),
        rotation=round(rotation[i], 3),
        inclination=round(inclination[i], 3)
    )

    filename = f"config_{i:04d}.yaml"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

print("✅ Class 0: 250 YAML files generated successfully!")
