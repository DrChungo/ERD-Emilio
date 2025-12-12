import pandas as pd
import matplotlib.pyplot as plt

temperatures = [12, 13, 11, 15, 16, 14, 10]

temperature_series = pd.Series(temperatures)

average = temperature_series.mean()
maximum = temperature_series.max()
minimum = temperature_series.min()

print("Media:", average)
print("Máximo:", maximum)
print("Mínimo:", minimum)

plt.figure(figsize=(8, 5))
plt.plot(temperature_series)
plt.title("Temperaturas semanales")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.grid(True)

plt.show()
