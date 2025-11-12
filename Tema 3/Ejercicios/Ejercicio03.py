import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("notes.csv", encoding="utf-8")

# Verificación rápida de columnas
esperadas = {'Nom', 'Matemàtiques', 'Català', 'Anglès'}
if not esperadas.issubset(df.columns):
    raise ValueError(f"Faltan columnas en notes.csv. Debe contener: {esperadas}")

# ---------- 2) Barras: nota media por alumno ----------
df['Media'] = df[['Matemàtiques', 'Català', 'Anglès']].mean(axis=1)

plt.figure()
plt.bar(df['Nom'], df['Media'], label='Nota media')
plt.title('Nota media por alumno')
plt.xlabel('Alumno')
plt.ylabel('Nota media')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# ---------- 3) Circular: resultados encuesta ----------
# Sustituye estos valores por los de tu encuesta real
etiquetas = ["Me gusta Python", "Prefiero JavaScript", "Me es indiferente"]
valores = [45, 30, 25]  # ejemplo

plt.figure()
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
plt.title('Resultados de la encuesta')
plt.legend(etiquetas, title='Opciones', loc='best')
plt.tight_layout()
plt.show()

# ---------- 4) Líneas múltiples: ventas semanales de 3 productos ----------
# Ejemplo de dataset (puedes leerlo de CSV si lo tienes)
semanas = [f"S{i}" for i in range(1, 9)]
ventas = pd.DataFrame({
    'Semana': semanas,
    'Producto A': [120, 140, 130, 150, 160, 155, 165, 170],
    'Producto B': [80,  90,  95,  100, 110, 120, 115, 130],
    'Producto C': [60,  70,  65,  75,  85,  80,  95,  100],
})

plt.figure()
plt.plot(ventas['Semana'], ventas['Producto A'], marker='o', label='Producto A')
plt.plot(ventas['Semana'], ventas['Producto B'], marker='o', label='Producto B')
plt.plot(ventas['Semana'], ventas['Producto C'], marker='o', label='Producto C')
plt.title('Ventas semanales por producto')
plt.xlabel('Semana')
plt.ylabel('Unidades vendidas')
plt.legend(title='Producto')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# ---------- 5) Boxplot (Seaborn): distribución de notas ----------
# Usamos las columnas de asignaturas del CSV
notas_long = df.melt(
    id_vars='Nom',
    value_vars=['Matemàtiques', 'Català', 'Anglès'],
    var_name='Asignatura',
    value_name='Nota'
)

plt.figure()
sns.boxplot(data=notas_long, x='Asignatura', y='Nota')
plt.title('Distribución de notas por asignatura')
plt.xlabel('Asignatura')
plt.ylabel('Nota')
plt.tight_layout()
plt.show()
