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

donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()

Table = Jeu_de_donnees(data_un[0:30])

#print(Table)

table_mg = Moyenne_glissante().transform(Table, 7, "incid_rea")

print(Jointure_vertical().transform(Table, table_mg))

# New = Selection_variable().transform(Table, ["incid_rea"])
#
# print(Centrage().transform(New))

# Table.remove_column(position=-2)
# print(Table.column_names, Table.rows)