import pandas as pd

names = ["Anna", "Jordi", "Marta", "Pol", "Laia"]
grades = [7.5, 8.0, 6.0, 5.5, 9.0]

dataframe = pd.DataFrame({
    "Nombre": names,
    "Nota": grades
})

print(dataframe)
print()
print(dataframe.head(3))

max_grade = dataframe["Nota"].max()
min_grade = dataframe["Nota"].min()

print()
print("Nota maxima:", max_grade)
print("Nota minima:", min_grade)
