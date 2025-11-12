import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# DataFrame de animales
animals = ['León', 'Tigre', 'Elefante', 'Jirafa', 'Mono', 'Pingüino']
specimens = [5, 3, 2, 4, 10, 8]

df_zoo = pd.DataFrame({'Animal': animals, 'Ejemplares': specimens})
print(df_zoo)

#  Gráfico de barras
colores = ['gold', 'orange', 'gray', 'yellowgreen', 'saddlebrown', 'skyblue']

plt.bar(df_zoo['Animal'], df_zoo['Ejemplares'], color=colores)
plt.title('Número de ejemplares por animal en el zoo')
plt.xlabel('Animal')
plt.ylabel('Número de ejemplares')


for i, animal in enumerate(animals):
    plt.bar(0, 0, color=colores[i], label=animal)  

plt.legend(title='Animales')
plt.show()

#  Gráfico de líneas
days = list(range(1, 11))
prices = [10, 10.5, 11, 10.8, 11.2, 11.5, 12, 11.7, 12.2, 12.5]

plt.plot(days, prices, marker='o', color='green', label='Precio diario (€)')
plt.title('Evolución del precio del producto en 10 días')
plt.xlabel('Día')
plt.ylabel('Precio (€)')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de sectores:
# hacer grande para que se vea bien
actividades = ['Sueño', 'Clases', 'Ocio', 'Deporte', 'Comidas', 'Otros']
hours = [56, 35, 21, 7, 7, 14] 
act_color = ['purple', 'orange', 'lightgreen', 'red', 'pink', 'gray']

plt.pie(hours, labels=actividades, autopct='%1.1f%%', startangle=90, colors=act_color)
plt.title('Distribución semanal de tiempo')
plt.legend(actividades, title="Actividades", loc="best")
plt.show()

#  Histograma:
num = np.random.randint(0, 21, 100)

plt.hist(num, bins=10, color='cornflowerblue', edgecolor='black', label='Frecuencia de valores')
plt.title('Histograma de 100 números aleatorios entre 0 y 20')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()
