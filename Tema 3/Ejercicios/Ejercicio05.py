import pandas as pd
import matplotlib.pyplot as plt

# --- Leer dataset ---
df = pd.read_csv(r"C:\Users\Emiliano\Desktop\vsCode\ERD\ERD\Tema 3\Ejercicios\aeropuerto_palma.csv")
print(df)




#  Gráfico de líneas: evolución mensual de pasajeros
plt.figure(figsize=(8, 5))
plt.plot(df['Mes'], df['Pasajeros'], marker='o', color='dodgerblue', linewidth=2)
plt.title("Evolución mensual de pasajeros en el aeropuerto de Palma", fontsize=13)
plt.xlabel("Mes")
plt.ylabel("Número de pasajeros")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_lineas_pasajeros.png")
plt.show()

# 2 Gráfico de barras: comparación mensual
plt.figure(figsize=(8, 5))
plt.bar(df['Mes'], df['Pasajeros'], color='lightcoral', edgecolor='black')
plt.title("Pasajeros por mes (2024)", fontsize=13)
plt.xlabel("Mes")
plt.ylabel("Número de pasajeros")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_barras_pasajeros.png")
plt.show()

# Gráfico de sectores: participación relativa por trimestre

df['Trimestre'] = ['T1']*3 + ['T2']*3 + ['T3']*3 + ['T4']*3
df_quarter = df.groupby('Trimestre')['Pasajeros'].sum()

plt.figure(figsize=(6, 6))
plt.pie(df_quarter, labels=df_quarter.index, autopct='%1.1f%%',
        colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999'],
        startangle=90, explode=[0, 0.1, 0, 0])
plt.title("Distribución de pasajeros por trimestre", fontsize=13)
plt.tight_layout()
plt.savefig("grafico_sectores_trimestres.png")
plt.show()
