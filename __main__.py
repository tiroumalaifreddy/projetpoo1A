from estimators.estimators import Estimators
from transformers.transformers import Transformers
from transformers.conversion_csv import Conversion_CSV as cv

if __name__ == "__main__":
    estimators = Estimators()
    transformers = Transformers()
    estimators.fit()
    transformers.transform()

cv.conversion_en_csv("D:\Perso\ENSAI", "covid-hospit-incid-reg-2021-03-03-17h20.csv")

