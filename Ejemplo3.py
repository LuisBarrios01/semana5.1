#Escribir y importar datos de excel
import math

import xlrd
import pandas as pd
import numpy as np

datos = pd.read_excel('BI_Alumnos.xlsx', sheet_name='Hoja1')
minimo = pd.DataFrame(datos).min()
maximo = pd.DataFrame(datos).max()
r = maximo - minimo
n = pd.DataFrame(datos).count()
k = 1 + 3.3 * math.log10(n)
tic = r/k

print(minimo, maximo, r, n, k, tic)
print()
print('----------------------------------------------')
rango = np.arange(9.0, 15.3, 0.9)
frecuencia = pd.cut(datos['Nota'], rango)
tabla = pd.value_counts(frecuencia)
print(tabla)