[![MASS-UBMATF](https://img.shields.io/badge/MASS--UBMATF-Computational_Astrobiology_2026-blue)](COURSE_PAGE_URL)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20722949.svg)](https://doi.org/10.5281/zenodo.20722949)
# Recovering planetary transit signals in active PLATO-like stars using simulation and machine learning

# Detecting Exoplanet Transits in Active Stellar Environments Using Machine Learning

The search for exoplanets often relies on identifying tiny, periodic decreases in a star’s brightness caused by a planet crossing the stellar disk. While this task is relatively straightforward for quiet stars, stellar activity such as flares, rotational modulation, and starspots can distort light curves and make planetary transits significantly harder to detect.

This project investigates how stellar activity affects exoplanet transit detectability using a simulated PLATO-like dataset generated with the PLATO Solar-like Light-curve Simulator (PSLS). Four classes of light curves were analyzed:

* Class 0: No planet, no activity
* Class 1: Stellar activity only
* Class 2: Planet with low stellar activity
* Class 3: Planet with strong stellar activity

Three machine-learning approaches were evaluated:

* Random Forest
* XGBoost
* 1D Convolutional Neural Network (CNN)

Their performance was compared against the classical Transit Least Squares (TLS) transit-search algorithm.

The machine-learning models achieved excellent classification performance, with Random Forest reaching 100% accuracy, XGBoost 99.5%, and CNN 96.5%. In contrast, TLS recovered only 53.3% of the tested planetary systems under realistic stellar-variability conditions. These results demonstrate that machine-learning methods can remain highly effective even when stellar activity complicates classical transit detection.

Beyond model comparison, the project also explores how stellar variability, flare amplitude, spot size, stellar rotation, and transit depth influence recovery performance. The results suggest that stellar activity plays a more significant role in transit detectability than planetary size alone within the simulated dataset.

This repository contains the complete analysis pipeline, including dataset exploration, feature engineering, machine-learning classification, TLS baseline evaluation, and visualization notebooks used to investigate exoplanet detection in active stars.

## Dataset

The simulated dataset was generated using the PLATO Solar-like Light-curve Simulator (PSLS) and contains PLATO-inspired stellar light curves with varying levels of stellar activity and planetary transit signatures.

Full dataset archive:

DOI: https://doi.org/10.5281/zenodo.20722949

The repository includes a lightweight demonstration subset that allows the notebooks to run end-to-end without downloading the complete dataset.


### Main Findings

* Machine-learning approaches substantially outperform the classical TLS baseline.
* Random Forest provides the most robust overall performance.
* Stellar activity significantly impacts classical transit recovery.
* Transit depth alone cannot explain recovery differences between activity classes.
* Feature-based machine-learning models effectively separate planetary signals from stellar variability.



