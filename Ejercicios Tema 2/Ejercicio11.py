import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
day = np.arange(1, 39)
goals = [4, 0, 2, 1, 1, 3, 0, 4, 2, 1, 3, 3, 2, 0, 1, 4, 3, 2, 0, 2, 1, 4, 5, 3, 0, 2, 4, 1, 3, 2, 2, 0, 4, 1, 3, 4, 2, 0]


# Crear gráfico de líneas
plt.plot(day, goals, label="Rendiment", color='blue', marker='o')

# Encontrar el índice del valor máximo
max_index = np.argmax(goals)
max_goals = goals[max_index]
max_day = day[max_index]

# Marcar el máximo con un punto rojo
plt.scatter(max_day, max_goals, color='red', s=100, zorder=5, label=f"Màxim: {max_goals}")



# Títulos y etiquetas
plt.title("Grafico de goles por jornada")
plt.xlabel("Jornada")
plt.ylabel("goles")


# Mostrar gráfico
plt.grid(True)
plt.show()