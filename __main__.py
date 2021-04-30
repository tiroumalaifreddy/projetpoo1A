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


c_csv=Conversion('/Users/Mamadoudiallo/Downloads/', "test.csv")
data_un =c_csv.convert()

#print(*data_un[0:5], sep='\n')

c_json=Conversion('/Users/Mamadoudiallo/Downloads/', "VacancesScolaires.json")
data_deux=c_json.convert()
#print(*data_deux['Calendrier'], sep='\n')
#print(data_deux)
test={"a": 1, "b":2}
a=data_deux["Calendrier"]
cle1=[]
for i in range(len(a)):
    #print(i)
    cle=[]
    valeur=[]
    for key, value in a[i].items():
        valeur.append(value)
        if not key in cle:
            cle.append(key)
    cle1+=[valeur]
cle1.insert(0,cle)
#print(*cle1[0:20], sep='\n')
#print(cle)
#print(valeur)
#print(len(a))
b=data_deux["Academie"]
cle2=[]
for i in range(len(b)):
    #print(i)
    cles=[]
    valeurs=[]
    for key, value in b[i].items():
        valeurs.append(value)
        if not key in cles:
            cles+=[key]
    cle2+=[valeurs]
cle2.insert(0,cles)
print(*cle2[0:10],sep='\n')


