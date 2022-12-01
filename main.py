import math
import io
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})

#variabile utile
lista_ani = ['1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007']

#dictionare ultile
dictionar_tipuri = {
    "allCrime": pd.read_excel('../DataIn/fisier_excel.xlsx','Total', index_col=0),
    "homicide": pd.read_excel('../DataIn/fisier_excel.xlsx','Intentional homicide', index_col=0),
    "harm": pd.read_excel('../DataIn/fisier_excel.xlsx','Harm', index_col=0),
    "robbery": pd.read_excel('../DataIn/fisier_excel.xlsx','Robbery', index_col=0),
    "burglary": pd.read_excel('../DataIn/fisier_excel.xlsx','Burglary of private residential', index_col=0),
    "theft": pd.read_excel('../DataIn/fisier_excel.xlsx','Theft of a motorized land vehic', index_col=0),
    "unlawfulActs": pd.read_excel('../DataIn/fisier_excel.xlsx','Unlawful acts involving control', index_col=0)
}

dictionar_dataframes = {
    "allCrime": pd.DataFrame(data = dictionar_tipuri["allCrime"], columns=lista_ani),
    "homicide": pd.DataFrame(data = dictionar_tipuri["homicide"], columns=lista_ani),
    "harm": pd.DataFrame(data = dictionar_tipuri["harm"], columns=lista_ani),
    "robbery": pd.DataFrame(data = dictionar_tipuri["robbery"], columns=lista_ani),
    "burglary": pd.DataFrame(data = dictionar_tipuri["burglary"], columns=lista_ani),
    "theft": pd.DataFrame(data = dictionar_tipuri["theft"], columns=lista_ani),
    "unlawfulActs": pd.DataFrame(data = dictionar_tipuri["unlawfulActs"], columns=lista_ani)
}

matrice_diferenta_ani = {
    "allCrime": np.ndarray(shape=(len(dictionar_dataframes["allCrime"].index),len(dictionar_dataframes["allCrime"].columns)-2)),
    "homicide": np.ndarray(shape=(len(dictionar_dataframes["homicide"].index),len(dictionar_dataframes["homicide"].columns)-2)),
    "harm": np.ndarray(shape=(len(dictionar_dataframes["harm"].index),len(dictionar_dataframes["harm"].columns)-2)),
    "robbery": np.ndarray(shape=(len(dictionar_dataframes["robbery"].index),len(dictionar_dataframes["robbery"].columns)-2)),
    "burglary": np.ndarray(shape=(len(dictionar_dataframes["burglary"].index),len(dictionar_dataframes["burglary"].columns)-2)),
    "theft": np.ndarray(shape=(len(dictionar_dataframes["theft"].index),len(dictionar_dataframes["theft"].columns)-2)),
    "unlawfulActs": np.ndarray(shape=(len(dictionar_dataframes["unlawfulActs"].index),len(dictionar_dataframes["unlawfulActs"].columns)-2))
}

etichete_linii = dictionar_tipuri["allCrime"].index.values.tolist()
print('-----------------------------etichete_linii--------------------------------')
print(etichete_linii)
print('----------------------------------etichete_coloane---------------------------')
etichete_coloane = dictionar_tipuri["allCrime"].columns.values[0:].tolist()
print(etichete_coloane)
# print('----------------------------------X---------------------------')
# X = dictionar_tipuri["allCrime"][etichete_coloane].values
# print(X)

# Sa se calculeze diferenta intre ani si sa se adauge intr-o matrice. Matricea va fi salvata intr-un fisier csv
print('||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||')
coloane_m_diferenta_ani = [i + '-' + j for i, j in zip(lista_ani[1:], lista_ani)]
print(coloane_m_diferenta_ani)

print("``````````````````````````````````````````````````````````````````````````````````````")
print(dictionar_dataframes["theft"])


for key in matrice_diferenta_ani.keys():
    print(key)
    for i in range(len(dictionar_tipuri[key].index)):
        for j in range(len(dictionar_tipuri[key].columns)-2):
            matrice_temporara = matrice_diferenta_ani[key]
            matrice_temporara[i][j] = matrice_temporara[i][j + 1] - matrice_temporara[i][j]
            #matrice_diferenta_ani[i][j] = math.ceil((matrice_allCrime[i][j+1] - matrice_allCrime[i][j]))
            #matrice_diferenta_ani[key][i][j] = matrice_allCrime[key][i][j + 1] - matrice_allCrime[key][i][j]
            print(matrice_temporara[i][j])

            matrice_diferenta_ani[key] = matrice_temporara

#print(matrice_diferenta_ani)