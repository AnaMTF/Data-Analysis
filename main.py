import math
import io
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})

allCrime = pd.read_excel('../DataIn/fisier_excel.xlsx','Total', index_col=0)
homicide = pd.read_excel('../DataIn/fisier_excel.xlsx','Intentional homicide', index_col=0)
harm = pd.read_excel('../DataIn/fisier_excel.xlsx','Harm', index_col=0)
robbery = pd.read_excel('../DataIn/fisier_excel.xlsx','Robbery', index_col=0)
burglary = pd.read_excel('../DataIn/fisier_excel.xlsx','Burglary of private residential', index_col=0)
theft = pd.read_excel('../DataIn/fisier_excel.xlsx','Theft of a motorized land vehic', index_col=0)
unlawfulActs = pd.read_excel('../DataIn/fisier_excel.xlsx','Unlawful acts involving control', index_col=0)
#print(allCrime)
# print(homicide)
# print(harm)
# print(robbery)
# print(burglary)
# print(theft)
# print(unlawfulActs)

etichete_linii = allCrime.index.values.tolist()
print('-----------------------------etichete_linii--------------------------------')
print(etichete_linii)
print('----------------------------------etichete_coloane---------------------------')
etichete_coloane = allCrime.columns.values[0:].tolist()
print(etichete_coloane)
print('----------------------------------X---------------------------')
X = allCrime[etichete_coloane].values
print(X)

lista_ani = ['1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007']
df_allCrime = pd.DataFrame(data = allCrime, columns=lista_ani)
df_homicide = pd.DataFrame(data = homicide, columns=lista_ani)
df_harm = pd.DataFrame(data = harm, columns=lista_ani)
df_robbery = pd.DataFrame(data = robbery, columns=lista_ani)
df_burglary = pd.DataFrame(data = burglary, columns=lista_ani)
df_theft = pd.DataFrame(data = theft, columns=lista_ani)
df_unlawfulActs = pd.DataFrame(data = unlawfulActs, columns=lista_ani)

#matrice_homicide = utl.inlocuireNAN
#print(matrice_homicide)
#print(df_allCrime)

p1_allCrime = sns.heatmap(df_allCrime, vmin=0, vmax=1000000)
#plt.show()


# Sa se calculeze diferenta intre ani si sa se adauge intr-o matrice. Matricea va fi salvata intr-un fisier csv
print('||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||')
coloane_m_diferenta_ani = [i + '-' + j for i, j in zip(lista_ani[1:], lista_ani)]
print(coloane_m_diferenta_ani)

print("``````````````````````````````````````````````````````````````````````````````````````")
matrice_allCrime = allCrime.values
#print(matrice_allCrime)

#dictionare ultile
matrice_diferenta_ani = {
    "allCrime": np.ndarray(shape=(len(df_allCrime.index),len(df_allCrime.columns)-2)),
    "homicide": np.ndarray(shape=(len(df_homicide.index),len(df_homicide.columns)-2)),
    "harm": np.ndarray(shape=(len(df_harm.index),len(df_harm.columns)-2)),
    "robbery": np.ndarray(shape=(len(df_robbery.index),len(df_robbery.columns)-2)),
    "burglary": np.ndarray(shape=(len(df_burglary.index),len(df_burglary.columns)-2)),
    "unlawfulActs": np.ndarray(shape=(len(df_unlawfulActs.index),len(df_unlawfulActs.columns)-2))
}

#sugestie: sa le citesti direct in dictionar
dictionar_tipuri = {
    "allCrime": allCrime,
    "homicide": homicide,
    "harm": harm,
    "robbery": robbery,
    "burglary": burglary,
    "unlawfulActs": unlawfulActs
}

dictionar_dataframes = {
    "allCrime": df_allCrime,
    "homicide": df_homicide,
    "harm": df_harm,
    "robbery": df_robbery,
    "burglary": df_burglary,
    "unlawfulActs": df_unlawfulActs
}

#matrice_diferenta_ani = np.ndarray(shape=(len(df_allCrime.index),len(df_allCrime.columns)-2))
#print(type(matrice_diferenta_ani))
print('hello!', matrice_diferenta_ani['allCrime'])

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



######################################################################################################################
# concatenare theft roberry si burglary - totalfurturi
# df_scadere = pd.DataFrame(data = matrice_scadere,index=etichete_linii,  columns=coloane_matrice_scadere_ani) #mark
# print(df_scadere)
#
# #salvare in csv
# df_scadere.to_csv("dataOUT/Scaderea.csv")
#
# print("#############################")
#
# #Sa se realizeze suma anilor de pe fiecare spreadsheet acestea ulterior fiind salvate intr-un csv
#
# sum_all = ['Suma tuturor cauzelor este: '] + list(allDeath.sum())[0:]
# print(sum_all)
#
# sum_infectious = ['Suma deceselor cauzate de infectii este: '] + list(infectiousCauses.sum())[0:]
# print(sum_infectious)
#
# sum_mental =  ['Suma deceselor cauzate de boli psihice'] + list(mentalCauses.sum())[0:]
# print(sum_mental)
#
# sum_transport = ['Suma deceselor cauzate de accidente in trasnport'] + list(accidentCauses.sum())[0:]
# print(sum_transport)
#
# list_all = list(allDeath.sum())[0:]
# list_infectious = list(infectiousCauses.sum())[0:]
# list_mental = list(mentalCauses.sum())[0:]
# list_transport = list(accidentCauses.sum())[0:]
#
#
# df_sum = pd.DataFrame({'Suma cauze totale': list_all,
#                         'Suma cauze boli infectioase':list_infectious,
#                         'Suma cauze boli psihice' : list_mental,
#                         'Suma cauze accidente transport': list_transport}, index = etichete_coloane)
#
#
# print(df_sum)
#
# df_sum.to_csv("dataOUT/Suma.csv")
#
# print("#############################")
#
# #Sa se afle ce procent din cauzele totale reprezinta bolile infectioase, bolile psihice si accidentele de transport
#
# lista_procente_infetious = list()
# lista_procente_mental = list()
# lista_procente_accident = list()
#
# for i in range(len(list_infectious)):
#     lista_procente_infetious.append((list_infectious[i]*100)/list_all[i])
#
# print(lista_procente_infetious)
#
# for i in range(len(list_mental)):
#     lista_procente_mental.append((list_mental[i]*100)/list_all[i])
#
# print(lista_procente_mental)
#
# for i in range(len(list_transport)):
#     lista_procente_accident.append((list_transport[i]*100)/list_all[i])
#
# print(lista_procente_accident)
#
#
# df_procente = pd.DataFrame({'Procente cauze boli infectioase':lista_procente_infetious,
#                             'Procente cauze boli psihice' : lista_procente_mental,
#                             'Procente cauze accidente transport': lista_procente_accident}, index = etichete_coloane)
# print(df_procente)
#
#
# df_procente.to_csv("dataOUT/Procente.csv")
#
# print("#############################")
