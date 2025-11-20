import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




days = np.arange(1, 31)
min = np.random.randint(20, 90, size=30) 

df_ejercicio = pd.DataFrame({'Día': days, 'Minutos': min})
print("=== SEGUIMIENTO DEPORTIVO ===")
print(df_ejercicio)

# Histograma de la distribución
plt.hist(df_ejercicio['Minutos'], bins=8, edgecolor='black')
plt.title("Distribución de minutos de ejercicio")
plt.xlabel("Minutos")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de líneas con la evolución
plt.plot(df_ejercicio['Día'], df_ejercicio['Minutos'], marker='o')
plt.title("Evolución diaria del ejercicio físico")
plt.xlabel("Día")
plt.ylabel("Minutos de ejercicio")
plt.grid(True)
plt.show()





# Dataset: ingresos y gastos mensuales
month = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
income = [2000, 2100, 1950, 2200, 2300, 2100, 2000, 2150, 2250, 2400, 2350, 2500]
bills = [1800, 1750, 1900, 2000, 2100, 1950, 1850, 1900, 2000, 2100, 2050, 2200]

df_budget = pd.DataFrame({
    'Mes': month,
    'Ingresos': income,
    'Gastos': bills
})
df_budget['Ahorro'] = df_budget['Ingresos'] - df_budget['Gastos']
df_budget['Ahorro Acumulado'] = df_budget['Ahorro'].cumsum()

print("\n=== PRESUPUESTO FAMILIAR ===")
print(df_budget)

# Gráfico de barras apiladas (ingresos vs gastos)
plt.bar(df_budget['Mes'], df_budget['Ingresos'], label='Ingresos')
plt.bar(df_budget['Mes'], df_budget['Gastos'], label='Gastos')
plt.title("Comparativa de ingresos y gastos mensuales")
plt.xlabel("Mes")
plt.ylabel("Euros (€)")
plt.legend()
plt.show()

# Gráfico de líneas del ahorro acumulado
plt.plot(df_budget['Mes'], df_budget['Ahorro Acumulado'], marker='o', color='green')
plt.title("Evolución del ahorro acumulado")
plt.xlabel("Mes")
plt.ylabel("Ahorro acumulado (€)")
plt.grid(True)
plt.show()




# Dataset: temperaturas mínimas y máximas de 12 meses
temp_min = [5, 6, 8, 10, 13, 17, 20, 20, 17, 13, 9, 6]
temp_max = [14, 15, 17, 20, 24, 28, 31, 31, 27, 22, 17, 15]

df_weather = pd.DataFrame({
    'Mes': month,
    'Temp Mínima': temp_min,
    'Temp Máxima': temp_max
})
df_weather['Temp Media'] = (df_weather['Temp Mínima'] + df_weather['Temp Máxima']) / 2

print("\n=== CLIMA ===")
print(df_weather)

# Gráfico de líneas doble (mínima y máxima)
plt.plot(df_weather['Mes'], df_weather['Temp Mínima'], marker='o', label='Temp. mínima')
plt.plot(df_weather['Mes'], df_weather['Temp Máxima'], marker='o', label='Temp. máxima')
plt.title("Temperaturas mínimas y máximas mensuales")
plt.xlabel("Mes")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de barras con la temperatura media
plt.bar(df_weather['Mes'], df_weather['Temp Media'], color='orange', edgecolor='black')
plt.title("Temperatura media por mes")
plt.xlabel("Mes")
plt.ylabel("Temperatura media (°C)")
plt.show()
