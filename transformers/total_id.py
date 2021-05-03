from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Total_id(Transformers):

    def transform(self, Table, liste_index, index_variable_id = 0):
        liste_par_id = []
        liste_id = []
        for liste in Table.rows:
            if liste[index_variable_id] not in liste_id:
                liste_id.append(liste[index_variable_id])
        for id in liste_id:
            liste_somme = [0 for i in range(len(liste_index))]
            for liste in Table.rows:
                if liste[index_variable_id] == id:
                    for n in range(len(liste_somme)):
                        liste_somme[n] += float(liste[liste_index[n]])
            liste_somme.insert(0, id)
            liste_par_id.append(liste_somme)
        new_data = [[Table.column_names[k] for k in liste_index]]
        new_data[0].insert(0, Table.column_names[index_variable_id])
        new_data += liste_par_id
        return Jeu_de_donnees(new_data)



