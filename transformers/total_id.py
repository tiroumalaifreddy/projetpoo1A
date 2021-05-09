from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Total_id(Transformers):
    def __init__(self, liste_index, index_variable_id = 0 ):
        self.liste_index = liste_index
        self.index_variable_id = index_variable_id


    def transform(self, Table):
        liste_par_id = []
        liste_id = []
        for liste in Table.rows:
            if liste[self.index_variable_id] not in liste_id:
                liste_id.append(liste[self.index_variable_id])
        for id in liste_id:
            liste_somme = [0 for i in range(len(self.liste_index))]
            for liste in Table.rows:
                if liste[self.index_variable_id] == id:
                    for n in range(len(liste_somme)):
                        liste_somme[n] += float(liste[self.liste_index[n]])
            liste_somme.insert(0, id)
            liste_par_id.append(liste_somme)
        new_data = [[Table.column_names[k] for k in self.liste_index]]
        new_data[0].insert(0, Table.column_names[self.index_variable_id])
        new_data += liste_par_id
        return Jeu_de_donnees(new_data)



