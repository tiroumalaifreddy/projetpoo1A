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
from export_csv import Export_csv

# Question: Comment évolue la moyenne journalière des nouveaux décès et des nouvelles admissions en réanimation du mois de novembre par rapport au mois de avril ?
import time
start_time = time.time()

# my code here


Table = Jeu_de_donnees(Conversion(folder="/home/freddy/Downloads/", filename="donnees-hospitalieres-nouveaux-covid19-2021-05-12-19h05.csv").convert())


Table_confinement_1 = Pipeline().transform(Table, [Fenetrage("2020-04-01","2020-04-30", index_date=1), Selection_variable(["jour", "incid_rea", "incid_dc"]), Total_id([1, 2], index_variable_id=0)])
Table_confinement_2 = Pipeline().transform(Table, [Fenetrage("2020-11-01","2020-11-30", index_date=1), Selection_variable(["jour", "incid_rea", "incid_dc"]), Total_id([1, 2])])

print(round(Moyenne(1).fit(Table_confinement_1), 2), round(Moyenne(2).fit(Table_confinement_1), 2))
print(round(Moyenne(1).fit(Table_confinement_2), 2), round(Moyenne(2).fit(Table_confinement_2), 2))

Data = [["Moyenne_incid_rea_avril", "Moyenne_incid_rea_novembre", "Moyenne_incid_dc_avril", "Moyenne_incid_dc_novembre"],[round(Moyenne(1).fit(Table_confinement_1), 2), round(Moyenne(1).fit(Table_confinement_2), 2), round(Moyenne(2).fit(Table_confinement_1), 2), round(Moyenne(2).fit(Table_confinement_2), 2)]]

Table_export = Jeu_de_donnees(Data)

Export_csv().export(Table_export, "resultats_csv")


print("time elapsed: {:.2f}s".format(time.time() - start_time))