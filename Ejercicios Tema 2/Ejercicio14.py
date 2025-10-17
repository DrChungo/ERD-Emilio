import matplotlib.pyplot as plt

# Datos
genres = ["Tecno", "House", "EDM", "Dubstep"]
listeners = [120, 90, 60, 30]

# --- Gráfico de barras ---
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(genres, listeners, color=['#FF8C00', '#1E90FF', '#32CD32', '#FF6347'])
plt.title("cantidad de veces escuchada")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.grid(axis='y', linestyle='--', alpha=0.6)

# --- Gráfico circular ---
plt.subplot(1, 2, 2)
plt.pie(
    listeners,
    labels=genres,
   
    colors=['#FF8C00', '#1E90FF', '#32CD32', '#FF6347'],
    startangle=90
)
plt.title("Distribución de escuchas")

# Ajustar diseño y mostrar
plt.tight_layout()
plt.savefig("comparacion_graficos.png", dpi=300)
plt.show()

#Encuentro que es mas facil de barras por el contexto en el que estamos el otro creo que representa bien la informacion.
#Ya que no estamos hablando de porcentajes

