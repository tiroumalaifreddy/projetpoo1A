from estimators.estimators import Estimators
from transformers.transformers import Transformers
from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from transformers.selection_variable import Selection_variable
from transformers.moyenne_glissante import Moyenne_glissante
from transformers.fenetrage import Fenetrage
from estimators.moyenne import Moyenne
from estimators.ecart_type import Ecart_type
from transformers.centrage import Centrage
from transformers.normalisation import Normalisation

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()
print(data_un)
# print(data_un[0:5])
#
# selection_une = Selection_variable(data_un[0:5], ["incid_rea"])
# var = selection_une.select_multiple_var()
# #
# print(var)
# Nm = Normalisation()
# print(Nm.normalisation(var))

#
# C = Centrage()
#
# print(*C.centrage(var), sep="\n")

# E = Ecart_type()
#
# print(E.ecart_type_corr(var))

# print(*data_un, sep="\n")

# F = Fenetrage()
#
# print(*F.fenetrage(data_un, '2020-03-22', '2020-03-30'), sep="\n")

#print(*data_un, sep="\n")
#M = Moyenne_glissante()
#
#print(M.moyenne_glissante(data_un, 10, "incid_rea"))
#data_deux = donnees_brut.convert()
#
# J = Jointure_vertical(data_un, data_deux)
#
# print(*J.fusion_v(), sep = "\n")

#selection_une = Selection_variable(data_un, ["nomReg"])
#var_un = selection_une.select_multiple_var()
#print(*var_un, sep="\n")

# selection_deux = Selection_variable(data_un, "numReg")
# var_un = selection_une.select_une_var()
# var_deux = selection_deux.select_une_var()
# J_deux = Jointure_vertical(var_un, var_deux)
# jointure = J_deux.fusion_v()
#
# print(*jointure, sep="\n")