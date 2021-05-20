from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json, Separator
from examples import custom_style_3
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
import ast

questions_un = [
    {
        'type': 'input',
        'name': 'folder',
        'message': "Entrer l'emplacement du fichier"
    },
    {
        'type': 'input',
        'name': 'filename',
        'message': 'Enter le nom du fichier'
    },
    {
        'type': 'checkbox',
        'name': 'transform',
        'message': 'Quelles transformations souhaitez-vous appliquer ?',
        'choices': [
            {
                'name': 'Clean'

            },
            {
                'name': 'Fenetrage'

            },
            {
                'name': 'Selection_variable'
            },
            {
                'name': 'Total_id'

            }
        ]

    }
]

answers_un = prompt(questions_un)

Table = Jeu_de_donnees(Conversion(answers_un['folder'], answers_un['filename']).convert())

questions_fenetrage =[
    {
        'type': 'input',
        'name': 'date_debut',
        'message': 'Fenetrage: entrer le début de la période',
    },
    {
        'type': 'input',
        'name': 'date_fin',
        'message': 'Fenetrage: entrer la fin de la période',
    },
    {
        'type': 'input',
        'name': 'index_date',
        'message': "Fenetrage: entrer l'index de la variable date dans la table",
    }
]

questions_selection_variable = [
    {
        'type': 'input',
        'name': 'liste_variables',
        'message': 'Selection_variable: entrer la liste des variables choisies',
    }
]

questions_total_id = [
    {
        'type': 'input',
        'name': 'liste_index',
        'message': 'Total_id: entrer la liste des index des variables qui vont être sommées'
    },
    {
        'type': 'input',
        'name': 'index_variable_id',
        'message' : "Total_id: entrer l'index de la variable_id"
    }
]

for i in answers_un['transform']:
    if i=="Fenetrage":
        answers_fenetrage = prompt(questions_fenetrage)
        Table = Fenetrage(answers_fenetrage['date_debut'], answers_fenetrage['date_fin'], int(answers_fenetrage['index_date'])).transform(Table)
    if i=="Selection_variable":
        answers_selection_variable = prompt(questions_selection_variable)
        Table = Selection_variable(ast.literal_eval(answers_selection_variable['liste_variables'])).transform(Table)
    if i=="Total_id":
        answers_total_id = prompt(questions_total_id)
        Table = Total_id(ast.literal_eval(answers_total_id['liste_index']), int(answers_total_id['index_variable_id'])).transform(Table)

print(Table)

question_export = [
    {
        'type':'confirm',
        'name':'export_oui',
        'message':'Souhaitez-vous exporter la table ?'
    }
]

question_export_detail = [
    {
        'type':'input',
        'name':'export_det',
        'message':'entrer le nom du fichier'
    }
]

answer_export_oui = prompt(question_export)

if answer_export_oui["export_oui"]==True:
    answer_export_det = prompt(question_export_detail)
    Export_csv().export(Table, answer_export_det['export_det'])

