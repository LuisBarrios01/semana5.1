import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


archivo = pd.read_csv('WEO_Data.csv',thousands=',',decimal='.')
print(archivo)
archivo.rename(columns={'Country':'Pais'},inplace=True)
archivo.set_index('Pais',inplace=True)
lista1=list(map(str,range(2000,2024)))

def grafico1():
    peru = archivo.loc['Peru',lista1]
    peru.plot()
    plt.show()

grafico1()

def grafico1_2():
    peru1 = archivo.loc['Peru', lista1]
    peru1.plot(kind='line')
    plt.title('PERU-PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

grafico1_2()

def grafico2():
    peru_chile = archivo.loc[['Peru','Chile'], lista1]
    peru_chile = peru_chile.transpose()
    peru_chile.plot(kind='line')
    plt.title('PERU y CHILE -PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

grafico2()

def grafico3():
    archivo.sort_values(by='2022',ascending=False,inplace=True)
    top5 = archivo[lista1].head(5)
    top5 = top5.transpose()
    top5.plot(kind='line')
    plt.title('Los 5 1eros  paises con mayor pbi -PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

grafico3()

def grafico4():
    archivo['2022'].plot(kind='hist')
    plt.title('PBI-PAISES')
    plt.ylabel('Billones de $')
    plt.xlabel('Años')
    plt.show()

grafico4()

def grafico5():
    barras = archivo.loc['Peru', lista1]
    barras.plot(kind='bar')
    plt.title('PERU-PBI')
    plt.ylabel('Millones de $')
    plt.xlabel('Años')
    plt.show()

grafico5()

def grafico6():
    archivo.sort_values(by='2022',ascending=False,inplace=True)
    lista10 = archivo['2022'].tail(10)
    lista10 = lista10.transpose()
    lista10.plot(kind='barh')
    plt.title('Los 10 ultimos paises -PBI')
    plt.ylabel('Billones de $')
    plt.xlabel('Años')
    plt.show()

grafico6()
