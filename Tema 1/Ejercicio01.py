import pandas as pd
import csv
import json

# #dades = pd.read_csv(r'C:\Users\user\Desktop\Workbook1.csv')
# dades = pd.read_csv(r'C:\Users\Emiliano\vsCode\ERD\Tema 1\Ejercicio01.csv')
# print(dades)+



# # Read CSV file
# df = pd.read_csv('C:\Users\Emiliano\vsCode\ERD\Tema 1\Ejercicio01.csv')

# # DataFrame to JSON
# df.to_json('Ejercicio01.json', orient='records', lines=True)



df = pd.read_csv(r"C:\Users\Emiliano\vsCode\ERD\Tema 1\Ejercicio01.csv")


df.to_json(r"C:\Users\Emiliano\vsCode\ERD\Tema 1\Ejercicio01.json", orient="records")