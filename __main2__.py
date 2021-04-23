from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.selection_variable import Selection_variable
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
from transformers.normalisation import Normalisation
from transformers.centrage import Centrage

donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()

Table = Jeu_de_donnees(data_un[0:5])

New = Selection_variable().transform(Table, ["incid_rea"])

print(Centrage().transform(New))

# Table.remove_column(position=-2)
# print(Table.column_names, Table.rows)