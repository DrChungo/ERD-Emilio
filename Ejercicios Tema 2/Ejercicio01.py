import matplotlib.pyplot as plt

months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
avg_temperatures = [6, 7, 10, 14, 18, 22, 25, 24, 21, 16, 11, 7]

plt.figure(figsize=(8, 5))
plt.plot(months, avg_temperatures, marker='o', linestyle='-', color='b')
plt.title("Temperatura media mensual")
plt.xlabel("Meses")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()