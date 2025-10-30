import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Generem 50 notes aleatòries entre 4 i 10
notes = np.random.uniform(4, 10, 50)  # números decimals uniformes entre 4 i 10

# 2. Fem el gràfic amb histograma i corba de densitat
sns.histplot(notes, kde=True, bins=10, color="purple")

# 3. Afegim títol i etiquetes per fer-ho més maco

plt.title("Distribució de 50 notes aleatòries (4 - 10)")
plt.xlabel("Nota")
plt.ylabel("Freqüència")

plt.show()