#Escribir y importar datos de excel
import xlrd
import pandas as pd
import numpy as np

datos = pd.read_excel('BI_Clientes.xlsx', sheet_name='Hoja1')
rango = np.arange(-1, 6, 1)
total_hijos = pd.cut(datos['TotalChildren'], rango)
tabla = pd.value_counts(total_hijos)
print(tabla)