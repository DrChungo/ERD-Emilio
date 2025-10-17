import matplotlib.pyplot as plt

months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
counts = [5, 6, 9, 13, 17, 3]
counts2 = [7, 2, 4, 7, 8, 9]

plt.plot(months, counts, label="Serie 1", marker='o')
plt.plot(months, counts2, label="Serie 2", marker='s')
plt.title("Comparativa de ventas por mes")
plt.xlabel("Meses")
plt.ylabel("Cantidad vendida")
plt.legend()
plt.grid(True)
plt.show()