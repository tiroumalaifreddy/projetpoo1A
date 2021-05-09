from datetime import date as dt
from datetime import timedelta
from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers



class Fenetrage(Transformers):
    def __init__(self, date_debut, date_fin, index_date = 0):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.index_date = index_date

    def transform(self, Table):
        liste_date = []
        for i in range((dt.fromisoformat(self.date_fin) - dt.fromisoformat(self.date_debut)).days + 1):
            liste_date.append(str(dt.fromisoformat(self.date_debut) + timedelta(days=i)))
        new_data = [Table.column_names]
        for date in liste_date:
            for liste in Table.rows:
                if liste[self.index_date] == date:
                    new_data.append(liste)
        return Jeu_de_donnees(new_data)



