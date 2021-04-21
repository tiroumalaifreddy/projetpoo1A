from estimators.estimators import Estimators
from transformers.transformers import Transformers
from transformers.conversion import Conversion
from transformers.jointure_vertical import Jointure_vertical
from transformers.moyenne_glissante import Moyenne_glissante as mo

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

<<<<<<< HEAD
c_csv=cv('/Users/Mamadoudiallo/Downloads/', "test.csv")
data_un = c_csv.conversion_en_csv()
data_deux = c_csv.conversion_en_csv()
test=mo.moyenne_glissante(data_un,10)
J = Jointure_vertical(data_un, data_deux)
#print(*test, sep='\n')
=======
donnees_brut = Conversion('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = donnees_brut.convert()

>>>>>>> 9fbfaa155488aa811fc24128a794200ce8c8eeee



<<<<<<< HEAD
#print(c_json.conversion_en_json())
=======
>>>>>>> 9fbfaa155488aa811fc24128a794200ce8c8eeee
