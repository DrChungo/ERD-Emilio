import matplotlib.pyplot as plt
# Exemple: Vendes mensuals
mesos = ["Gener", "Febrer", "Març", "Abril", "Maig"]
vendes = [100, 120, 90, 140, 160]
plt.plot(mesos, vendes, marker="o", color="blue")
plt.title("Vendes mensuals")
plt.xlabel("Mesos")
plt.ylabel("Unitats venudes")
plt.show()