import pandas as pd
import numpy as np


data = {
    "Nombre": ["Ana", "Marc", "Julia", "Ana", "Pau", "Yago Lopez"],
    "Nota": [8.5, 7.0, 4.0, 8.5, 9.0, 2.7],
   
}

sales = {
    "producto": ["Mesa", "Silla", "Lámpara", "Sofa"],
    "cantidad": [5, 15, 8, 20],
    "precio": [50, 30, 20, 200]
}
df = pd.DataFrame(data)



df["Aprovado"] = df["Nota"] >= 5
df["Aprovado"]=df["Aprovado"].map({True:"si",False:"no"})


df_sales=pd.DataFrame(sales)
df_filtered= df_sales[df_sales["cantidad"]>10]
print("\nProductos con mas de 10 unidades vendidas\n", df_filtered)

print("Notas alumnos\n",df)

df_sorted=df.sort_values(by="Nota",ascending=False)
print("\nAlumnos ordenados por nota de mayor a menor:\n", df_sorted)