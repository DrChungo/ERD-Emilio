import matplotlib.pyplot as plt
import random



fig, ax = plt.subplots()

notes = ["0-2", "2-4", "4-6", "6-8", "8-10"]
counts = [random.randint(0, 120) for _ in range(5)]
print(counts)

bar_labels = ["0-2", "2-4", "4-6", "6-8", "8-10"]
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']

bars=ax.bar(notes, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('cantidad de alumnos')
ax.set_xlabel("notas")
ax.set_title('Distribucion de notas')


ax.legend(bars,bar_labels, title='Notas')

plt.show()