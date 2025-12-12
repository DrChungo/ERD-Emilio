import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Dia": ["Dl", "Dl", "Dt", "Dt", "Dc", "Dc", "Dj", "Dj"],
    "Visites": [120, 150, 130, 160, 140, 170, 110, 180]
}

dataframe = pd.DataFrame(data)

print("DataFrame original:")
print(dataframe)

grouped = dataframe.groupby("Dia")["Visites"].mean()

print("\nMedia de visitias por dia:")
print(grouped)

plt.figure(figsize=(8, 5))
plt.bar(grouped.index, grouped.values)
plt.title("Media visitas por dia")
plt.xlabel("Dia")
plt.ylabel("Media de visitas")

plt.show()
