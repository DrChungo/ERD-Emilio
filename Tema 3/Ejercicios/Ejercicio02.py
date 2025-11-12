import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1) DataFrame con notas

students = ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fabio', 'Gema', 'Hugo']
mathNotes = [7.5, 6.0, 8.0, 5.5, 9.0, 7.0, 6.5, 8.5]
languageNotes = [6.0, 7.0, 7.5, 6.5, 8.0, 6.0, 7.0, 9.0]

df_notes = pd.DataFrame({
    'Alumno': students,
    'Matemáticas': mathNotes,
    'Lengua': languageNotes
})
print("DataFrame de notas:\n", df_notes, "\n")


# 2) Gráfico de barras apilado 

x = np.arange(len(students))
width = 0.6 

plt.figure()
plt.bar(x, df_notes['Matemáticas'], width=width, label='Matemáticas', color='steelblue')
plt.bar(x, df_notes['Lengua'], width=width, bottom=df_notes['Matemáticas'], label='Lengua', color='lightcoral')
plt.xticks(x, students, rotation=0)
plt.title('Notas por alumno (apiladas)')
plt.xlabel('Alumno')
plt.ylabel('Nota')
plt.ylim(0, 20)  
plt.legend(title='Asignatura')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()


# 3 doble línea

days = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
t_min = [8, 7, 9, 10, 11, 9, 8]
t_max = [16, 17, 18, 20, 19, 18, 17]

plt.figure()
plt.plot(days, t_min, marker='o', label='Mínima (°C)')
plt.plot(days, t_max, marker='o', label='Máxima (°C)')
plt.title('Temperaturas semanales: mínima y máxima')
plt.xlabel('Día')
plt.ylabel('Temperatura (°C)')
plt.legend(title='Serie')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()


# Gráfico de dispersión

height_cm = [150, 155, 160, 162, 165, 168, 170, 172, 175, 178, 180, 185]
weight_kg   = [45, 50, 52, 54, 57, 60, 63, 66, 70, 74, 77, 85]

plt.figure()
plt.scatter( height_cm,  weight_kg, label='Alumnos', s=60)
plt.title('Relación entre altura y peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()


# 5) Barras 

months = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
income = [2100, 2100, 2150, 2150, 2200, 2200, 2200, 2200, 2250, 2250, 2300, 2300]
bills   = [1800, 1750, 1900, 1850, 1950, 2000, 1950, 1900, 2000, 2050, 2100, 2150]

x = np.arange(len(months))
w = 0.35

plt.figure()
plt.bar(x - w/2, income, width=w, label='Ingresos', color='mediumturquoise')
plt.bar(x + w/2, bills,   width=w, label='Gastos',   color='tomato')
plt.xticks(x, months, rotation=0)
plt.title('Ingresos vs Gastos mensuales (familia)')
plt.xlabel('Mes')
plt.ylabel('€')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)



balance = np.array(income) - np.array(bills)
for i, val in enumerate(balance):
    plt.text(i, max(income[i], bills[i]) + 30, f'Bal: {val:+}', ha='center', fontsize=8)
plt.show()
