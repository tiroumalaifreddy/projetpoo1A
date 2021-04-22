from datetime import date as dt
from datetime import timedelta



class Fenetrage():
    def fenetrage(self, data, date_debut, date_fin, index_date = 0):
        liste_date = []
        for i in range((dt.fromisoformat(date_fin) - dt.fromisoformat(date_debut)).days + 1):
            liste_date.append(str(dt.fromisoformat(date_debut) + timedelta(days=i)))
        new_data = []
        for date in liste_date:
            for liste in data:
                if liste[index_date] == date:
                    new_data.append(liste)
        return new_data



