import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Matemàtiques': [5, 6, 7, 8, 9, 10, 4, 7, 8, 5, 9, 6],
    'Història': [6, 6, 5, 7, 7, 8, 5, 6, 7, 6, 7, 5],
    'Anglès': [4, 5, 9, 10, 3, 7, 8, 10, 6, 9, 5, 8]
}


df = pd.DataFrame(data)


sns.boxplot(data=df)

plt.title("Distribució de notes per assignatura 📊")
plt.ylabel("Nota")
plt.xlabel("Assignatura")


plt.show()