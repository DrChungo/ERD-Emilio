
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta al CSV (ajústala si lo guardas en otro lugar)
df = pd.read_csv(r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 3\Ejercicios\notas.csv", encoding="utf-8")

# ---------- 2) Barras: nota media por alumno ----------
df['Media'] = df[['Matematicas', 'Catalan', 'Ingles']].mean(axis=1)

plt.figure()
plt.bar(df['Nombre'], df['Media'], label='Nota media', color='skyblue')
plt.title('Nota media por alumno')
plt.xlabel('Alumno')
plt.ylabel('Nota media')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# ---------- 3) Circular: resultados encuesta ----------
etiquetas = ["Me gusta Python", "Prefiero JavaScript", "Me es indiferente"]
valores = [45, 30, 25]

plt.figure()
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Resultados de la encuesta')
plt.legend(etiquetas, title='Opciones', loc='best')
plt.tight_layout()
plt.show()

# ---------- 4) Líneas múltiples ----------
weeks = [f"S{i}" for i in range(1, 9)]
ventas = pd.DataFrame({
    'Semana': weeks,
    'Producto A': [120, 140, 130, 150, 160, 155, 165, 170],
    'Producto B': [80,  90,  95,  100, 110, 120, 115, 130],
    'Producto C': [60,  70,  65,  75,  85,  80,  95,  100],
})

plt.figure()
plt.plot(ventas['Semana'], ventas['Producto A'], marker='o', label='Producto A')
plt.plot(ventas['Semana'], ventas['Producto B'], marker='s', label='Producto B')
plt.plot(ventas['Semana'], ventas['Producto C'], marker='^', label='Producto C')
plt.title('Ventas semanales por producto')
plt.xlabel('Semana')
plt.ylabel('Unidades vendidas')
plt.legend(title='Producto')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# ---------- 5) Boxplot (Seaborn): distribución de notas ----------
notes_long = df.melt(
    id_vars='Nombre',
    value_vars=['Matematicas', 'Catalan', 'Ingles'],
    var_name='Asignatura',
    value_name='Nota'
)

plt.figure()
sns.boxplot(data=notes_long, x='Asignatura', y='Nota', palette='pastel')
plt.title('Distribución de notas por asignatura')
plt.xlabel('Asignatura')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()
