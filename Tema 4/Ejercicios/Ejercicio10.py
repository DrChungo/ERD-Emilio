import pandas as pd
import matplotlib.pyplot as plt


dataframe = pd.read_csv(r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 4\Ejercicios\ventas.csv")

print("DATAFRAME CARGADO:")
print(dataframe)
print("\n")


print("ESTADÍSTICAS GENERALES:")
print(dataframe.describe())
print("\n")


plt.figure(figsize=(8,5))
plt.bar(dataframe["Producto"], dataframe["Ventas"])
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(dataframe["Precio"], dataframe["Ventas"])
plt.title("Relación entre precio y ventas")
plt.xlabel("Precio (€)")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()

correlation = dataframe["Precio"].corr(dataframe["Ventas"])
print(f"Correlación entre precio y ventas: {correlation:.3f}")


                            #CONCLUSIONES

    # Los productos más baratos se venden más. Se ve que cuando el precio es bajo, la gente compra más unidades.

    # Hay productos que se venden mucho más que otros. Por ejemplo, algunos tienen muchas ventas y otros muy pocas. Se nota rápido en el gráfico de barras.

    # El precio influye en las ventas. Aunque no cambie mucho, si sube un poco el precio, normalmente bajan las ventas.
