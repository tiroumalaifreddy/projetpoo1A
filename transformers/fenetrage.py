from datetime import date as dt
from datetime import timedelta
from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers



class Fenetrage(Transformers):
    def transform(self, Table, date_debut, date_fin, index_date = 0):
        liste_date = []
        for i in range((dt.fromisoformat(date_fin) - dt.fromisoformat(date_debut)).days + 1):
            liste_date.append(str(dt.fromisoformat(date_debut) + timedelta(days=i)))
        new_data = [Table.column_names]
        for date in liste_date:
            for liste in Table.rows:
                if liste[index_date] == date:
                    new_data.append(liste)
        return Jeu_de_donnees(new_data)



