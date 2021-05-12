from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.selection_variable import Selection_variable
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
from transformers.normalisation import Normalisation
from transformers.centrage import Centrage
from transformers.fenetrage import Fenetrage
from transformers.moyenne_glissante import Moyenne_glissante
from transformers.jointure_vertical import Jointure_vertical
from transformers.selection_ligne import Selection_ligne
from transformers.agregation import Agregation
from transformers.total_id import Total_id
from transformers.clean import Clean
from estimators.kmeans import Kmeans
from sklearn.cluster import KMeans as Km
import numpy as np
from transformers.pipeline import Pipeline
from export_csv import Export_csv
from Export_map.cartoplot import CartoPlot
import matplotlib as plt

donnees_brut = Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-03-03-17h03.csv")

data = donnees_brut.convert()

Table = Jeu_de_donnees(data)
F = Fenetrage('2021-02-23', '2021-02-23', index_date=1).transform(Table)
print(F)
# P = Pipeline().transform(Table, [Fenetrage('2021-02-25','2021-03-03', index_date=1), Selection_variable(['dep', 'incid_hosp']), Total_id([1]), Selection_ligne("dep", ["971","972","973","974","975"],symbole="!=")])
#
# Carte = CartoPlot()
#
# d = {}
#
# for i in range(len(P.rows)):
#     d[str(i)] = i
#
# d['69D'] = d['69']
# d['69M'] = d['69']
# del(d['69'])
# d['2A'] = 14
# d['2B'] = 13
#
# MAP = Carte.plot_dep_map(d, x_lim=(-6, 10), y_lim=(41, 52))
# MAP.savefig("fig4.png")


# Table = Fenetrage('2020-03-19', '2020-03-26').transform(Table)
# Table = Selection_variable(['incid_rea']).transform(Table)
# # #
# # #
# Table = Normalisation().transform(Table)
#
# X = np.array(Table.rows)
#
# K = Kmeans(2, 500).fit(Table)
# # #
# Kmea = Km(n_clusters=2, random_state=0).fit(X)
# print(K)
# print(Kmea.labels_)

# Table = Clean().transform(Table, remove=True)
#
# print(Kmeans().fit(Table, 3, 50))



# Table_sept_derniers_jours = Fenetrage().transform(Table, '2020-03-18', '2020-03-24', 0)
#
# new_Table = Selection_variable().transform(Table_sept_derniers_jours, ['incid_rea'])
# new_Table = Normalisation().transform(new_Table)
# print(new_Table)
# kmeans = Kmeans().fit(new_Table, 3)
# print(kmeans.cluster_centers_)


#print(*Table_sept_derniers_jours.rows, sep = '\n')
#new_Table = Total_id().transform(Table_sept_derniers_jours, [3], 2)
#print(new_Table)
# for liste in Table_sept_derniers_jours.rows:
#     if liste[2] =='84':
#         print(liste)
#print(Agregation().transform(Table, 0, "nb", "region"))

# data_un = donnees_brut.convert()
#
# Table = Jeu_de_donnees(data_un[0:5])
# print(Table)
#print(Selection_ligne().transform(Table, variable='incid_rea', liste_valeur=['7', '40'], symbole="<>"))

#print(Moyenne().fit(Selection_ligne().transform(Table, 'nomReg', ['Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comté']), 'incid_rea'))

#print(Table, sep="\n")

#table_mg = Moyenne_glissante().transform(Table, 2, "incid_rea")

#print(table_mg)

# New = Selection_variable().transform(Table, ["incid_rea"])
#
# print(Centrage().transform(New))

# Table.remove_column(position=-2)
# print(Table.column_names, Table.rows)