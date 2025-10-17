import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
StHours= np.random.randint(0,11,50)

notes= StHours*0.6 + np.random.normal(4,0.8,50)

sns.scatterplot(x=StHours, y=notes ,color="blue", label="Datos")


plt.title("Relacion de horas de estudio / notas")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota")
plt.show()

#Cuantas mas horas de estudio mejores notas
