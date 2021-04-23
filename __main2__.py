from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from Data.Jeu_de_donnees import Jeu_de_donnees

donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()

Table = Jeu_de_donnees(data_un[0:5])

Table.add_row([1,2,3,4])
print(Table.rows)