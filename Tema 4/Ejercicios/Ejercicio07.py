import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Edad": [18, 19, 20, 21, 22, 23, 24, 25],
    "Altura": [160, 162, 165, 168, 170, 172, 175, 178]
}

dataframe = pd.DataFrame(data)

print(dataframe)

plt.figure(figsize=(8, 5))
plt.scatter(dataframe["Edad"], dataframe["Altura"])
plt.title("Relación entre Edad y Altura")
plt.xlabel("Edad")
plt.ylabel("Altura (cm)")
plt.grid(True)

plt.show()

correlation = dataframe["Edad"].corr(dataframe["Altura"])
print("Coeficiente de correlación:", correlation)


                            #CORRELACION
        # Al aumentar la edad, también aumenta la altura. Esto significa que hay una correlación positiva: las dos cosas suben juntas.

