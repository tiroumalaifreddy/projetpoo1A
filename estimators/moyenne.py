class Moyenne():
    def moyenne(self, data, variable):
        somme = 0
        index_variable = data[0].index(variable)
        for liste in data[1:]:
            somme += float(liste[index_variable])
        return somme/len(data[1:])

