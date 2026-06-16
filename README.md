[![MASS-UBMATF](https://img.shields.io/badge/MASS--UBMATF-Computational_Astrobiology_2026-blue)](COURSE_PAGE_URL)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20722949.svg)](https://doi.org/10.5281/zenodo.20722949)
# Recovering planetary transit signals in active PLATO-like stars using simulation and machine learning

This project focuses on generating synthetic PLATO-like stellar light curves for exoplanet transit detection under different stellar activity conditions.

### Features

- Synthetic light-curve generation
- Planetary transit injection
- Stellar activity simulation
- YAML-based parameter configuration
- Metadata CSV construction
- Statistical analysis and visualization
- Transit Least Squares (TLS) baseline detection
- Preparation for ML/DL classification

---

# Dataset Classes

- Class 0 → Quiet star without planet
- Class 1 → Active star without planet
- Class 2 → Planet with moderate stellar activity
- Class 3 → Planet with strong stellar activity

---

# Files

- `notebooks/` → Jupyter notebook analysis
- `scripts/` → Python scripts
- `data/` → Metadata and sample light curves
- `configs/` → YAML configuration files
- `figures/` → Generated plots and TLS outputs

---

# Current Progress

- Metadata generation completed
- Statistical analysis completed
- Light-curve visualization completed
- Flux variability comparison completed
- TLS transit detection baseline completed
- Wotan detrending
- Random Forest classification
- XGBoost classification
- 1D CNN implementation

---

# Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Astropy
- Transit Least Squares (TLS)
- Jupyter Notebook


