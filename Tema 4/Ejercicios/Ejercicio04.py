import pandas as pd
import matplotlib.pyplot as plt

products = ["Cafe", "Te", "Sandwich", "Galleta", "Zumo"]
sales = [120, 85, 45, 60, 95]

dataframe = pd.DataFrame({
    "Producto": products,
    "Ventas": sales
})

print("DataFrame completo:")
print(dataframe)

filtered = dataframe[dataframe["Ventas"] > 80]

print("\nProductos con más de 80 ventas:")
print(filtered)

plt.figure(figsize=(8, 5))
plt.bar(filtered["Producto"], filtered["Ventas"])
plt.title("Productos con mas de 80 ventas")
plt.xlabel("Producto")
plt.ylabel("Ventas")

plt.tight_layout()
plt.show()
