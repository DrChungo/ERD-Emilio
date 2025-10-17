import matplotlib.pyplot as plt
import numpy as np
species = ('Futbol', 'Baloncesto', 'Voley')
sex_counts = {
    'Male': np.array([12, 10, 5]),
    'Female': np.array([6, 8, 12]),
}
width = 0.6  
fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Cantidad de alumnos por deporte')
ax.legend()

plt.show()