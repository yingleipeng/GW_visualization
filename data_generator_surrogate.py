from NRSur7dq2 import NRSurrogate7dq2
import numpy as np
import pandas as pd

sur = NRSurrogate7dq2()

q_values = [1.2, 1.5, 1.8, 2.0]  # Mass ratios
all_rows = []

for q in q_values:
    chiA = np.array([0.0, 0.0, 0.0])
    chiB = np.array([0.0, 0.0, 0.0])

    try:
        modes, chiA_t, chiB_t = sur(q, chiA, chiB, return_spins=True)
        quat, phi_orb, chiA_dyn, chiB_dyn = sur.get_dynamics(q, chiA, chiB)
        quat = quat.T
    except Exception as e:
        print(f"Error for q={q}: {e}")
        continue

    t = sur.t_coorb  # 2000 pts
    h22 = modes[2, 2]  # Dominant mode

    phi = -np.unwrap(np.angle(h22)) / 2.0
    omega = np.gradient(phi, t)
    r = (1.0 / (omega ** 2 + 1e-8)) ** (1 / 3)

    omega_0 = omega[0]
    r_0 = r[0]

    # Filtramos solo t entre -4500 y 0 (excluyendo lo que está fuera de ese rango)
    valid_indices = np.where((t >= -4500) & (t <= 0))[0]

    for i in valid_indices:
        row = {
            "time": t[i],
            "q": q,
            "r": r[i],
            "r_0": r_0,
            "omega": omega[i],
            "omega_0": omega_0,
            "h22_real": h22[i].real,
            "h22_imag": h22[i].imag,
            "phi": phi[i],
        }
        all_rows.append(row)

df = pd.DataFrame(all_rows)
df.to_csv("precessing_waveform_dataset3.csv", index=False)
print("Dataset filtered and saved to precessing_waveform_dataset.csv")


