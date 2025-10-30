import matplotlib.pyplot as plt

labels = ['WhatsApp', 'TikTok', 'Instagram', 'Twitter', 'Facebook']
sizes = [40, 40, 10, 5, 5]

# Crear una figura con 1 fila y 2 columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # figsize para que no se aplasten

# --- Gráfico de pastel ---
ax1.pie(sizes, labels=labels, startangle=90)
ax1.set_title("Uso por plataforma")

# --- Gráfico de barras ---
ax2.bar(labels, sizes, color=['green', 'red', 'purple', 'blue', 'navy'])
ax2.set_ylabel("Porcentaje de uso")
ax2.set_title("Uso por plataforma en barras")



plt.show()