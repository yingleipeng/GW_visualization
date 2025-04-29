# BBH Inspiral Modelling with PN and PINN Methods

This repository contains tools to model binary black hole (BBH) inspirals using two approaches:

- **Post-Newtonian (PN) approximations** up to 3.5PN order
- A **Physics-Informed Neural Network (PINN)** trained on surrogate waveforms

---

## What’s Included

- `binary_inspiral.ipynb`  
  Main notebook for computing and comparing BBH dynamics using PN and PINN models.

- `data_generator_surrogate.py`  
  Script to generate waveform training data from the `NRSur7dq2` surrogate model.

- `precessing_waveform_dataset3.csv`  
  Dataset used to train the PINN. Includes orbital and waveform data for several mass ratios.

- `plots/`  
  Visual results: dynamics, waveforms, and orbit comparisons.

---

## Methods

### Post-Newtonian
- 2.5PN and 3.5PN expansions implemented
- Integrated using 4th-order Runge-Kutta
- Waveforms generated via quadrupole approximation

### PINN (Physics-Informed Neural Network)
- Predicts waveform components and orbital dynamics
- Inputs: time \( t \), mass ratio \( q \)
- Outputs: \( r(t), \omega(t), \phi(t), h_+(t), h_\times(t) \)
- Loss includes physical constraints (Kepler’s law, phase-frequency matching)

---

## Requirements

- Python 3.8+
- Libraries:
  - `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `torch`, `scipy`
  - [`NRSurrogate`](https://github.com/sxs-collaboration/nr_surrogate) (for data generation)

Install requirements:
```bash
pip install numpy pandas matplotlib scikit-learn torch scipy
pip install nr-surrogate
