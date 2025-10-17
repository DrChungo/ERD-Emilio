import matplotlib.pyplot as plt

browsers = ["Chrome", "Firefox", "Safari", "Otros"]
percentages = [65, 20, 10, 5]
colors = ["blue", "orange", "green", "gray"]

plt.figure(figsize=(6, 6))
plt.pie(percentages, labels=browsers, startangle=140, colors=colors)
plt.title("Uso de navegadores web")
plt.axis("equal")  # mantiene el gráfico circular
plt.show()