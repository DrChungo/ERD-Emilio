import matplotlib.pyplot as plt

fruits = ["Manzana", "Plátano", "Naranja", "Fresa", "Uva"]
people = [25, 30, 15, 20, 10]
colors = ["red", "yellow", "orange", "pink", "purple"]

plt.figure(figsize=(8, 5))
plt.bar(fruits, people, color=colors)
plt.title("Fruta preferida")
plt.xlabel("Fruta")
plt.ylabel("Número de personas")
plt.show()
