import numpy as np
import pandas as pd
import seaborn as sns
from utile import *
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.f' % x)
np.set_printoptions(suppress=True, formatter={'float_kind': '{:f}'.format})

# Variabile utile
lista_ani = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
             '2006', '2007']

# Dictionare utile
dictionar_tipuri = {
    "allCrime": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Total', index_col=0),
    "homicide": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Intentional homicide', index_col=0),
    "harm": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Harm', index_col=0),
    "robbery": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Robbery', index_col=0),
    "burglary": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Burglary of private residential', index_col=0),
    "theft": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Theft of a motorized land vehic', index_col=0),
    "unlawfulActs": pd.read_excel('./DataIn/fisier_excel.xlsx', 'Unlawful acts involving control', index_col=0)
}

dictionar_dataframes = {
    "allCrime": pd.DataFrame(data=dictionar_tipuri["allCrime"], columns=lista_ani),
    "homicide": pd.DataFrame(data=dictionar_tipuri["homicide"], columns=lista_ani),
    "harm": pd.DataFrame(data=dictionar_tipuri["harm"], columns=lista_ani),
    "robbery": pd.DataFrame(data=dictionar_tipuri["robbery"], columns=lista_ani),
    "burglary": pd.DataFrame(data=dictionar_tipuri["burglary"], columns=lista_ani),
    "theft": pd.DataFrame(data=dictionar_tipuri["theft"], columns=lista_ani),
    "unlawfulActs": pd.DataFrame(data=dictionar_tipuri["unlawfulActs"], columns=lista_ani)
}

matrice_diferenta_ani = {
    "allCrime": dictionar_dataframes["allCrime"].to_numpy(copy=True),
    "homicide": dictionar_dataframes["homicide"].to_numpy(copy=True),
    "harm": dictionar_dataframes["harm"].to_numpy(copy=True),
    "robbery": dictionar_dataframes["robbery"].to_numpy(copy=True),
    "burglary": dictionar_dataframes["burglary"].to_numpy(copy=True),
    "theft": dictionar_dataframes["theft"].to_numpy(copy=True),
    "unlawfulActs": dictionar_dataframes["unlawfulActs"].to_numpy(copy=True)
}

dictionar_liste = {
    'allCrime': list(dictionar_tipuri['allCrime'].sum())[0:],
    'homicide': list(dictionar_tipuri['homicide'].sum())[0:],
    'harm': list(dictionar_tipuri['harm'].sum())[0:],
    'robbery': list(dictionar_tipuri['robbery'].sum())[0:],
    'burglary': list(dictionar_tipuri['burglary'].sum())[0:],
    'theft': list(dictionar_tipuri['theft'].sum())[0:],
    'unlawfulActs': list(dictionar_tipuri['unlawfulActs'].sum())[0:]
}

dictionar_procente = {
    'homicide': [],
    'harm': [],
    'robbery': [],
    'burglary': [],
    'theft': [],
    'unlawfulActs': []
}

# DataFrame ce contine date pentru scatter plot
date_venit_crima = pd.read_excel("./DataIn/comparatie_earnings_crime.xlsx", 'Tabel', index_col=0)

# Etichete pentru DataFrames
etichete_linii = dictionar_tipuri["allCrime"].index.values.tolist()
etichete_coloane = dictionar_tipuri["allCrime"].columns.values[0:].tolist()
coloane_m_diferenta_ani = [i + '-' + j for i, j in zip(lista_ani[1:], lista_ani)]

# Calcule folosind ndarray bidimensional

# Sa se calculeze diferenta intre ani si sa se adauge intr-o matrice. Matricea va fi salvata intr-un fisier csv
for key in matrice_diferenta_ani.keys():
    marime = matrice_diferenta_ani[key].shape[1]
    temporar = matrice_diferenta_ani[key]

    for i in reversed(range(1, marime)):
        temporar[:,i] = temporar[:,i] - temporar[:,i-1]

    matrice_diferenta_ani[key] = temporar
    matrice_out = pd.DataFrame(matrice_diferenta_ani[key], index=etichete_linii).drop(columns=0)
    matrice_out.columns = coloane_m_diferenta_ani
    matrice_out.to_csv(f"./DataOut/fisiere_csv/diferenta_ani_{key}.csv")

# Sa se calculeze cat % reprezinta fiecare crima din numarul total de crime pentru fiecare tara in anul 2006
for key in dictionar_procente.keys():
    lista_temp_all = dictionar_liste['allCrime']
    for i in range(len(dictionar_liste[key])):
        lista_temp = dictionar_liste[key]

        dictionar_procente[key].append(lista_temp[i]*100/lista_temp_all[i])
    print(dictionar_procente[key])

# -- Grafice --

# Heatmap pentru toate infractiunile cu scopul de a observa variatia
# numarului de infractiuni in functie de an si de tari

fig, ax = plt.subplots(figsize=(10,10))
heatmap = sns.heatmap(dictionar_dataframes["allCrime"], vmin=0, vmax=1000000,cmap=sns.cubehelix_palette(as_cmap=True),linewidth=.1,ax=ax)
heatmap.set(xlabel='Intervalul de ani', ylabel='Tarile')
heatmap.set_title('Variatia infractiunilor in toate tarile de-a lungul anilor')
#plt.show()


# ScatterPlot pentru a calcula corelatia dintre venitul din 2006 si
# rata criminalitatii la 100.000 de locuitori

x_values = date_venit_crima["2006E"].values.tolist()
y_values = date_venit_crima["CR"].values.tolist()

scatter_plot_date = pd.DataFrame({"x_values": x_values, "y_values": y_values})

plt.plot('x_values', 'y_values', data=scatter_plot_date, linestyle='none', marker='o',)
#plt.show()

sns.regplot(x=date_venit_crima["2006E"], y=date_venit_crima["CR"], line_kws={"color":"r"})
#plt.show()

#Line Chart pentru numarul mediu de furturi in fiecare an din toate tarile

lista_valori_medie_furt = []

marime_coloane = len(etichete_coloane)
marime_linii = len(etichete_linii)
temporar_theft = dictionar_dataframes["theft"]
temporar_burglary = dictionar_dataframes["burglary"]
temporar_robbery = dictionar_dataframes["robbery"]

#print(temporar_theft)

for an in lista_ani:
    suma = temporar_theft[an].sum() + temporar_burglary[an].sum() + temporar_robbery[an].sum()
    medie = suma/marime_linii
    lista_valori_medie_furt.append(medie)

plt.plot(lista_valori_medie_furt)
#plt.show()
