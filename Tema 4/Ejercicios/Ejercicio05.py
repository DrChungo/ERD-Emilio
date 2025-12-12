import matplotlib.pyplot as plt

categories = ["Comida", "Transporte", "Ocio", "Otros"]
expenses = [300, 70, 120, 50]

plt.figure(figsize=(7, 7))
plt.pie(expenses, labels=categories, autopct='%1.1f%%')
plt.title("Distribución del gasto mensual")

plt.show()
