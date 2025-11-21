import pandas as pd
import matplotlib.pyplot as plt

# Activar estilo seaborn

plt.style.use("seaborn-v0_8")

# 1) Gráfico de barras: hábitos semanales
habitos = {
    'Hábito': ['Sueño', 'Estudio', 'Deporte', 'Pantallas'],
    'Horas (semana)': [56, 18, 6, 25]  # Ejemplo: 8h/día de sueño, etc.
}
df_habitos = pd.DataFrame(habitos)

plt.bar(
    df_habitos['Hábito'],
    df_habitos['Horas (semana)'],
    color=['#4C78A8', '#F58518', '#54A24B', '#E45756']  # Colores personalizados
)
plt.title("Hábitos semanales (horas totales)")
plt.xlabel("Hábito")
plt.ylabel("Horas a la semana")
plt.show()


# 2) Gráfico de dispersión: altura vs edad de la clase
alumnos = {
    'Edad':       [12, 13, 12, 14, 13, 12, 14, 13, 12, 14, 13, 12, 13, 14, 12],
    'Altura_cm':  [148, 155, 150, 165, 158, 149, 166, 157, 151, 164, 159, 150, 156, 167, 149]
}
df_clase = pd.DataFrame(alumnos)

plt.scatter(
    df_clase['Edad'],
    df_clase['Altura_cm'],
    c='#6C5B7B',
    edgecolor='black',
    s=80
)
plt.title("Altura vs Edad (clase)")
plt.xlabel("Edad (años)")
plt.ylabel("Altura (cm)")
plt.grid(True)
plt.show()


# 3) Gráfico de barras: usuarios de redes sociales (encuesta)
rrss = {
    'Red': ['Instagram', 'TikTok', 'Twitter', 'YouTube'],
    'Usuarios': [18, 22, 9, 25]  # Números de ejemplo
}
df_rrss = pd.DataFrame(rrss)

plt.bar(
    df_rrss['Red'],
    df_rrss['Usuarios'],
    color=['#C44E52', '#55A868', '#4C72B0', '#8172B2']
)
plt.title("Usuarios por red social (encuesta en clase)")
plt.xlabel("Red social")
plt.ylabel("Número de usuarios")
plt.show()
