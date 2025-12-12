import pandas as pd
import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023]
sales = [40000, 42000, 39500, 45000]

dataframe = pd.DataFrame({
    "Año": years,
    "Ventas": sales
})

print("DataFrame original:")
print(dataframe)

dataframe["Crecimiento"] = dataframe["Ventas"].diff()

print("\nDataFrame con crecimiento:")
print(dataframe)

plt.figure(figsize=(8, 5))
plt.plot(dataframe["Año"], dataframe["Ventas"])
plt.title("Evolución de ventas anuales")
plt.xlabel("Año")
plt.ylabel("Ventas")
plt.grid(True)

plt.show()
