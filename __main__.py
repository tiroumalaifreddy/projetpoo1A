from estimators.estimators import Estimators
from transformers.transformers import Transformers
from transformers.conversion_csv import Conversion_CSV as cv
from transformers.conversion_json import Conversion_json as cj
from transformers.jointure_vertical import Jointure_vertical

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

c_csv=cv('D:/Perso/ENSAI/', "covid-hospit-incid-reg-2021-03-03-17h20.csv")

data_un = c_csv.conversion_en_csv()
data_deux = c_csv.conversion_en_csv()

J = Jointure_vertical(data_un, data_deux)
print(*J.fusion_v(), sep='\n')


#c_json=cj('D:/Perso/ENSAI/', "VacancesScolaires.json")

#print(c_json.conversion_en_json())