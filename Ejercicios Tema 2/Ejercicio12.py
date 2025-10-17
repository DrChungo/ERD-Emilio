import pandas as pd
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv(r"C:\Users\Emiliano\Desktop\vsCode\ERD\Tema 1\Ejercicios Tema 2\Ejercicio12.csv")





"""

#barras
plt.bar(df['Mes'], df['Ventas'], color='green')
plt.title("Ventas mensuales en barras")
plt.xlabel("Mes")
plt.ylabel("ventas")
plt.xticks(rotation=45)

"""
"""

#Lineas
plt.plot(df['Mes'], df['Ventas'], marker='o', color='green')
plt.title("Evolucion de ventas  en lineas")
plt.xlabel("Mes")
plt.ylabel("Ventas (€)")
plt.xticks(rotation=45)
plt.grid(True)




"""
#Historiograma
plt.hist(df['Ventas'], bins=6, color='orange', edgecolor='black')
plt.title("Distribucion de ventas en histograma")
plt.xlabel("Ventas")
plt.ylabel("Frequencia")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()