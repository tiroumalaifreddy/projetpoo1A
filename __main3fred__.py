from estimators.estimators import Estimators
from transformers.transformers import Transformers
from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from transformers.selection_variable import Selection_variable

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()
# data_deux = donnees_brut.convert()
#
# J = Jointure_vertical(data_un, data_deux)
#
# print(*J.fusion_v(), sep = "\n")

selection_une = Selection_variable(data_un, "nomReg")
selection_deux = Selection_variable(data_un, "numReg")
var_un = selection_une.select_une_var()
var_deux = selection_deux.select_une_var()
J_deux = Jointure_vertical(var_un, var_deux)
jointure = J_deux.fusion_v()

print(*jointure, sep="\n")