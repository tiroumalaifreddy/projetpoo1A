from estimators.moyenne import Moyenne

M = Moyenne()

class Ecart_type():
    def ecart_type_corr(self, data):
        et = 0
        for liste in data[1:]:
            et += (float(liste[0]) - M.moyenne(data))**2
        return round((et/(len(data[1:])-1))**(0.5), 2)