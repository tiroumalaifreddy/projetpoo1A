from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical

donnees_brut = Conversion('D:/Perso/ENSAI/', "VacancesScolaires.json")

data = donnees_brut.convert()
print(data)