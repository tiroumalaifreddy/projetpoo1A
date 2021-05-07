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
from estimators.kmeans import Kmeans
from transformers.clean import Clean
from estimators.kmeans import Kmeans


donnees_brut = Conversion(folder = "/home/freddy/Documents/", filename="covid-hospit-incid-reg-2021-03-03-17h20.csv")

data = donnees_brut.convert()

Table = Jeu_de_donnees(data)
print(Table.rows)

# Table = Fenetrage().transform(Table, '2020-03-19', '2020-03-26')
# Table = Selection_variable().transform(Table, ['incid_rea'])
# #
# #
# Table = Normalisation().transform(Table)

# K = Kmeans().fit(Table, 3, 100)
# #
# print(K)

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