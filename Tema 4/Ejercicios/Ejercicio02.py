import pandas as pd
import matplotlib.pyplot as plt

names = ["Anna", "Jordi", "Marta", "Pol", "Laia"]
grades = [7.5, 8.0, 6.0, 5.5, 9.0]

dataframe = pd.DataFrame({
    "Nombre": names,
    "Nota": grades
})

plt.figure(figsize=(8, 5))
plt.bar(dataframe["Nom"], dataframe["Nota"])
plt.title("Notas de los alumnos")
plt.xlabel("Alumno")
plt.ylabel("Nota")

plt.tight_layout()
plt.show()
