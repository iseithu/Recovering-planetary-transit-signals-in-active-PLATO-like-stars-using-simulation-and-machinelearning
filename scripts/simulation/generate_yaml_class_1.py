import random
import os

output_dir = "generated_yaml_class_1"

os.makedirs(output_dir, exist_ok=True)

with open("templateclass1.yaml") as f:
    template = f.read()

for i in range(250):

    values = {

        "id": i,

        "mag": round(random.uniform(9,12),2),

        "rotation": round(
            random.uniform(5,30),
            2
        ),

        "inclination": round(
            random.uniform(0,90),
            2
        ),

        "sigma": round(
            random.uniform(300,800),
            2
        ),

        "tau": round(
            random.uniform(4,10),
            2
        ),

        "spot_radius":
            [round(random.uniform(3,6),1)
             for _ in range(3)],

        "spot_latitudes":
            [0.0, 20.0, 40.0],
               
        "spot_lifetime":
            [random.randint(10,60)
             for _ in range(3)],

        "spot_contrast":
            [round(random.uniform(0.5,0.9),2)
             for _ in range(3)],

        "flare_period":
            round(random.uniform(2,6),2),

        "flare_amplitude":
            round(random.uniform(500,1500),2)
    }

    content = template.format(**values)

    filename = (
        f"{output_dir}/"
        f"config_{i:04d}.yaml"
    )

    with open(filename,"w") as out:
        out.write(content)

print("250 YAML files created.")




