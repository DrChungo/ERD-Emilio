import matplotlib.pyplot as plt

# Datos de ejemplo
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3.5, 1.5, 4, 3]


plt.plot(
    x_values, 
    y_values, 
    color='yellow',       
    linewidth=3,               
    marker='o',             
    markersize=8,            
    markerfacecolor='red',   
    markeredgecolor='black'   
)


plt.title("Evolución de Datos en el Tiempo\n(Subtítulo: valores simulados)", fontsize=14, fontweight='bold')


plt.xlabel("Tiempo (s)")
plt.ylabel("Valor medido")


plt.legend(["Serie A"], loc='upper left')



plt.savefig("graf.png", dpi=300, bbox_inches='tight')

plt.show()
