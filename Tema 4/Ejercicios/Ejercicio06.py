import numpy as np
import matplotlib.pyplot as plt

grades = np.random.randint(0, 11, 30)

print("Notas generadas:")
print(grades)

plt.figure(figsize=(8, 5))
plt.hist(grades, bins=11, range=(0, 11), edgecolor="black")
plt.title("Distribución de notas del examen")
plt.xlabel("Nota")
plt.ylabel("Número de alumnos")
plt.xticks(range(0, 11))

plt.show()

values, counts = np.unique(grades, return_counts=True)
max_count = np.max(counts)

top_ranges = values[counts == max_count]

print("\nNota(s) con más alumnos:", top_ranges)
print("Número de alumnos en ese/eses rango(s):", max_count)
