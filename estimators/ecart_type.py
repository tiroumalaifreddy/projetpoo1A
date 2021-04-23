from estimators.moyenne import Moyenne as M



class Ecart_type():
    def ecart_type_corr(self, data, variable):
        et = 0
        index_variable = data[0].index(variable)
        for liste in data[1:]:
            et += (float(liste[index_variable]) - M().moyenne(data, variable))**2
        return round((et/(len(data[1:])-1))**(0.5), 2)



