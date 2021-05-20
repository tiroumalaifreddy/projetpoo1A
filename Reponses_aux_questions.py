from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.ecart_type import Ecart_type
from estimators.kmeans import Kmeans
from estimators.moyenne import Moyenne
from transformers.agregation import Agregation
from transformers.centrage import Centrage
from transformers.clean import Clean
from transformers.conversion import Conversion
from transformers.fenetrage import Fenetrage
from transformers.jointure_vertical import Jointure_vertical
from transformers.moyenne_glissante import Moyenne_glissante
from transformers.normalisation import Normalisation
from transformers.selection_ligne import Selection_ligne
from transformers.selection_variable import Selection_variable
from transformers.total_id import Total_id
from transformers.pipeline import Pipeline
from Export_map.cartoplot import CartoPlot
from datetime import date, timedelta


#Question 1: Quel est le nombre total d'hospitalisations dues au Covid-19 ?

Q1 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Desktop/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q1 = Pipeline().transform(Q1, [Agregation(0, "incid_hosp", echelle="region"), Agregation(0, "incid_hosp", echelle="nationale")])

print(Q1)
"""
['incid_hosp']
[478224.0]
"""



#Question 2: Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ?

Q2 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Desktop/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q2 = Pipeline().transform(Q2, [Fenetrage("2021-05-03", "2021-05-09", index_date=1), Selection_variable(["dep", "incid_hosp"]),Total_id([1])])
Selection_variable(["dep", "incid_hosp"]),
print(Q2)
"""
['dep', 'incid_hosp']
['01', 61.0]
['02', 111.0]
['03', 39.0]
['04', 20.0]
['05', 16.0]
['06', 65.0]
['07', 33.0]
['08', 25.0]
['09', 13.0]
['10', 37.0]
['11', 36.0]
['12', 34.0]
['13', 371.0]
['14', 72.0]
['15', 17.0]
['16', 24.0]
['17', 49.0]
['18', 26.0]
['19', 21.0]
['21', 55.0]
['22', 46.0]
['23', 5.0]
['24', 40.0]
['25', 38.0]
['26', 58.0]
['27', 36.0]
['28', 63.0]
['29', 33.0]
['2A', 9.0]
['2B', 5.0]
['30', 71.0]
['31', 84.0]
['32', 5.0]
['33', 113.0]
['34', 120.0]
['35', 112.0]
['36', 25.0]
['37', 101.0]
['38', 156.0]
['39', 30.0]
['40', 12.0]
['41', 51.0]
['42', 131.0]
['43', 19.0]
['44', 73.0]
['45', 84.0]
['46', 2.0]
['47', 19.0]
['48', 12.0]
['49', 68.0]
['50', 45.0]
['51', 69.0]
['52', 43.0]
['53', 15.0]
['54', 86.0]
['55', 19.0]
['56', 63.0]
['57', 109.0]
['58', 20.0]
['59', 392.0]
['60', 170.0]
['61', 54.0]
['62', 150.0]
['63', 61.0]
['64', 25.0]
['65', 13.0]
['66', 32.0]
['67', 154.0]
['68', 64.0]
['69', 308.0]
['70', 16.0]
['71', 73.0]
['72', 75.0]
['73', 53.0]
['74', 56.0]
['75', 472.0]
['76', 170.0]
['77', 213.0]
['78', 164.0]
['79', 34.0]
['80', 77.0]
['81', 32.0]
['82', 25.0]
['83', 99.0]
['84', 101.0]
['85', 47.0]
['86', 32.0]
['87', 58.0]
['88', 54.0]
['89', 39.0]
['90', 72.0]
['91', 217.0]
['92', 302.0]
['93', 328.0]
['94', 296.0]
['95', 208.0]
['971', 78.0]
['972', 31.0]
['973', 57.0]
['974', 77.0]
['976', 13.0]
"""
Carte = CartoPlot()

d = {}

for i in range(len(Q2.rows)):
    d[str(i)] = i

d['69D'] = d['69']
d['69M'] = d['69']
del(d['69'])
d['2A'] = 14
d['2B'] = 13

MAP = Carte.plot_dep_map(d, x_lim=(-6, 10), y_lim=(41, 52))
MAP.savefig("Q2.png") # visualisation du résultat sur fond de carte


#Question 3: Comment évolue la moyenne des nouvelles hospitalisations journalières de cette semaine par rapport à celle de la semaine dernière ?

Q3 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Desktop/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q3_semaine_derniere = Pipeline().transform(Q3, [Fenetrage("2021-04-26", "2021-05-02", index_date=1), Selection_variable(["jour","incid_hosp"]), Total_id([1])])
Q3_semaine_actuelle = Pipeline().transform(Q3, [Fenetrage("2021-05-03", "2021-05-09", index_date=1), Selection_variable(["jour","incid_hosp"]), Total_id([1])])

print(Moyenne(1).fit(Q3_semaine_actuelle) - Moyenne(1).fit(Q3_semaine_derniere)) #On a en moyenne 392 hospitalisations de moins par jour en moyenne
                                                                                 #par rapport à la semaine dernière
"""
-391.7142857142858
"""


#Question 4: Quel est le résultat de k-means avec k=3 sur les données des départements du mois de Janvier 2021,lissées avec une moyenne glissante de 7 jours ?

Q4_part1 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-covid19-2021-05-09-19h08.csv").convert())
Q4_part2 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Desktop/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q4_part1 = Pipeline().transform(Q4_part1, [Fenetrage("2021-01-01", "2021-01-31", 2), Selection_ligne("sexe", ["0"]), Selection_variable(["dep","hosp", "rea", "rad", "dc"])])
Q4_part2 = Pipeline().transform(Q4_part2, [Fenetrage("2021-01-01", "2021-01-31", 1), Selection_variable(["incid_hosp", "incid_rea", "incid_rad", "incid_dc"])])



Q4 = Jointure_vertical(Q4_part2).transform(Q4_part1)
Q4_kmeans = Pipeline().transform(Q4, [Clean(remove=True),
                                      Moyenne_glissante(7,["hosp", "rea", "rad", "dc", "incid_hosp", "incid_rea", "incid_rad", "incid_dc"]),
                                      Total_id([9,10,11,12,13,14,15,16], index_variable_id=0),
                                      Selection_variable(["M_glissante n7 de hosp", "M_glissante n7 de rea",
                                                          "M_glissante n7 de rad", "M_glissante n7 de dc",
                                                          "M_glissante n7 de incid_hosp", "M_glissante n7 de incid_rea",
                                                          "M_glissante n7 de incid_rad", "M_glissante n7 de incid_dc"]),

                                      Normalisation()])

res_kmeans = Kmeans(3, 100).fit(Q4_kmeans)
print(res_kmeans)
"""
[2 2 2 2 2 2 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 2 2 2
 2 1 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 1 1 0 0 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0
 0 0 1 1 1 2 2 2 2 2 2 2 1 0 0 0 0 0 0 0 1 2 2 2 2 2 2]
"""

#Question 5: Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?


Dates = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="VacancesScolaires.json").convert(choix="Calendrier"))

Dates_Toussaint = Pipeline().transform(Dates, [Selection_ligne("annee_scolaire", ["2020-2021"]), Selection_ligne("Description", ["Vacances de la Toussaint"]), Selection_variable(["Debut", "Fin"])])

# Les dates des vacances de la Toussaint sont les mêmes, quelque soit la zone.
date_fin = Dates_Toussaint.rows[0][1]
date_fin_plus_6 = (date.fromisoformat(date_fin) + timedelta(days=6)).isoformat()

Q5 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Desktop/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q5 = Pipeline().transform(Q5, [Fenetrage(date_fin, date_fin_plus_6, index_date=1), Selection_variable(["dep", "incid_rea"]), Agregation(0, "incid_rea", echelle="region"),Agregation(0, "incid_rea", echelle="nationale")])

print(Q5)
"""
['incid_rea']
[3037.0]
"""
