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

"""
#Question 1: Quel est le nombre total d'hospitalisations dues au Covid-19 ?

Q1 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q1 = Pipeline().transform(Q1, [Agregation(0, "incid_hosp", echelle="region"), Agregation(0, "incid_hosp", echelle="nationale")])

print(Q1) # On obtient 25797 hospitalisations au total.


"""
"""
#Question 2: Combien de nouvelles hospitalisations ont eu lieu ces 7 derniers jours dans chaque département ?

Q2 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q2 = Pipeline().transform(Q2, [Fenetrage("2021-05-03", "2021-05-09", index_date=1), Selection_variable(["dep", "incid_hosp"]), Total_id([1])])

print(Q2)

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

Q3 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q3_semaine_derniere = Pipeline().transform(Q3, [Fenetrage("2021-04-26", "2021-05-02", index_date=1), Selection_variable(["jour","incid_hosp"]), Total_id([1])])
Q3_semaine_actuelle = Pipeline().transform(Q3, [Fenetrage("2021-05-03", "2021-05-09", index_date=1), Selection_variable(["jour","incid_hosp"]), Total_id([1])])

print(Moyenne(1).fit(Q3_semaine_actuelle) - Moyenne(1).fit(Q3_semaine_derniere)) #On a en moyenne 392 hospitalisations de moins par jour en moyenne par rapport à la semaine dernière


"""
#Question 4: Quel est le résultat de k-means avec k=3 sur les données des départements du mois de Janvier 2021,lissées avec une moyenne glissante de 7 jours ?
"""
Q4_part1 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-covid19-2021-05-09-19h08.csv").convert())
Q4_part2 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q4_part1 = Pipeline().transform(Q4_part1, [Fenetrage("2021-01-01", "2021-01-31", 2), Selection_ligne("sexe", ["0"]), Selection_variable(["hosp", "rea", "rad", "dc"])])

Q4 = Jointure_vertical(Q4_part2).transform(Q4_part1)
Q4_d = Pipeline().transform(Q4, [Moyenne_glissante(7,["hosp", "rea", "rad", "dc"]), Selection_variable(["M_glissante n7 de hosp","M_glissante n7 de rea","M_glissante n7 de rad","M_glissante n7 de dc"])])

print(Q4_d)
"""

#K = Kmeans(3, 50).fit(Normalisation().transform(Q4))

#Question 5: Combien de nouvelles admissions en réanimation ont eu lieu pendant la semaine suivant les vacances de la Toussaint de 2020?

Dates = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="VacancesScolaires.json").convert(choix="Calendrier"))

Dates_Toussaint = Pipeline().transform(Dates, [Selection_ligne("annee_scolaire", ["2020-2021"]), Selection_ligne("Description", ["Vacances de la Toussaint"]), Selection_variable(["Debut", "Fin"])])

# Les dates des vacances de la Toussaint sont les mêmes, quelque soit la zone.
date_fin = Dates_Toussaint.rows[0][1]
date_fin_plus_6 = (date.fromisoformat(date_fin) + timedelta(days=6)).isoformat()

Q5 = Jeu_de_donnees(Conversion(folder = "/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-09-19h08.csv").convert())

Q5 = Pipeline().transform(Q5, [Fenetrage(date_fin, date_fin_plus_6, index_date=1), Selection_variable(["dep", "incid_rea"]), Agregation(0, "incid_rea", echelle="region"),Agregation(0, "incid_rea", echelle="nationale")])

print(Q5) # On a 3037 nouvelles admissions en réanimation.