import os
import yaml
import numpy as np
import pandas as pd

rows = []

for cls in range(4):

    yaml_dir = f"/home/zilani/Downloads/psls/generated_yaml_class_{cls}"
    dat_dir  = f"/home/zilani/Downloads/psls/output_class{cls}"

    yaml_files = sorted(
        [f for f in os.listdir(yaml_dir)
         if f.endswith(".yaml")]
    )

    dat_files = sorted(
        [f for f in os.listdir(dat_dir)
         if f.endswith(".dat")]
    )

    print(
        f"Class {cls}:",
        len(yaml_files),
        "yaml,",
        len(dat_files),
        "dat"
    )

    for yaml_file, dat_file in zip(yaml_files, dat_files):

        try:

            yaml_path = os.path.join(
                yaml_dir,
                yaml_file
            )

            dat_path = os.path.join(
                dat_dir,
                dat_file
            )

            with open(yaml_path) as f:
                cfg = yaml.safe_load(f)

            lc = np.loadtxt(dat_path)

            flux = lc[:,1]

            row = {

                "filename": dat_file,

                "class": cls,

                "planet_label":
                    int(cfg["Transit"]["Enable"]),

                "has_planet":
                    int(cfg["Transit"]["Enable"]),

                "has_activity":
                    int(cfg["Activity"]["Enable"]),

                "flux_mean":
                    np.mean(flux),

                "flux_std":
                    np.std(flux),

                "amplitude":
                    np.max(flux)-np.min(flux),

                "n_points":
                    len(flux),

                "planet_radius":
                    cfg["Transit"].get(
                        "PlanetRadius",0
                    ),

                "orbital_period":
                    cfg["Transit"].get(
                        "OrbitalPeriod",0
                    ),

                "impact_parameter":
                    cfg["Transit"].get(
                        "ImpactParameter",0
                    ),

                "flare_amplitude":
                    cfg["Activity"]
                    .get("Flare",{})
                    .get("Amplitude",0),

                "spot_radius_mean":
                    np.mean(
                        cfg["Activity"]
                        .get("Spot",{})
                        .get("Radius",[0])
                    ),

                "spot_latitude_mean":
                    np.mean(
                        cfg["Activity"]
                        .get("Spot",{})
                        .get("Latitude",[0])
                    ),

                "spot_lifetime_mean":
                    np.mean(
                        cfg["Activity"]
                        .get("Spot",{})
                        .get("Lifetime",[0])
                    ),

                "stellar_rotation_period":
                    cfg["Star"].get(
                        "SurfaceRotationPeriod",
                        0
                    ),

                "tau":
                    cfg["Activity"].get(
                        "Tau",
                        0
                    )
            }

            rows.append(row)

        except Exception as e:

            print(
                "ERROR:",
                cls,
                yaml_file,
                e
            )

metadata_v2 = pd.DataFrame(rows)
