import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.f' % x)
np.set_printoptions(suppress=True, formatter={'float_kind': '{:f}'.format})

# variabile utile
lista_ani = ['1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
             '2006', '2007']

# dictionare utile
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

# DataFrame ce contine date pentru scatter plot
date_venit_crima = pd.read_excel("./DataIn/comparatie_earnings_crime.xlsx", 'Tabel', index_col=0)

# etichete pentru DataFrames
etichete_linii = dictionar_tipuri["allCrime"].index.values.tolist()
etichete_coloane = dictionar_tipuri["allCrime"].columns.values[0:].tolist()
coloane_m_diferenta_ani = [i + '-' + j for i, j in zip(lista_ani[1:], lista_ani)]

# calcule folosind ndarray bidimensional

# Sa se calculeze diferenta intre ani si sa se adauge intr-o matrice. Matricea va fi salvata intr-un fisier csv
for key in matrice_diferenta_ani.keys():
    marime = matrice_diferenta_ani[key].shape[1]
    temporar = matrice_diferenta_ani[key]

    for i in reversed(range(1, marime)):
        temporar[:,i] = temporar[:,i] - temporar[:,i-1]

    matrice_diferenta_ani[key] = temporar
    matrice_out = pd.DataFrame(matrice_diferenta_ani[key], index=etichete_linii).drop(columns=0)
    matrice_out.columns = coloane_m_diferenta_ani
    matrice_out.to_csv(f"./DataOut/fisiere_cvs/diferenta_ani_{key}.csv")

# Grafice

# Heatmap pentru toate infractiunile cu scopul de a observa variatia
# numarului de infractiuni in functie de an si de tari

heatmap = sns.heatmap(dictionar_dataframes["allCrime"], vmin=0, vmax=1000000)

plt.show()

# ScatterPlot pentru a calcula corelatia dintre venitul din 2006 si
# rata criminalitatii la 100.000 de locuitori

x_values = date_venit_crima["2006E"].values.tolist()
y_values = date_venit_crima["CR"].values.tolist()

scatter_plot_date = pd.DataFrame({"x_values": x_values, "y_values": y_values})

plt.plot('x_values', 'y_values', data=scatter_plot_date, linestyle='none', marker='o')
plt.show()

#LineGraph pentru numarul mediu de crime in fiecare an din Romania
