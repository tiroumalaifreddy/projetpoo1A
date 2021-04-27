from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Selection_ligne(Transformers):
    def transform(self, Table, variable, liste_valeur, symbole = "="):
        index_variable = Table.column_names.index(variable)
        new_data = [Table.column_names]
        for liste in Table.rows:
            if symbole == "=":
                if liste[index_variable] in liste_valeur:
                    new_data.append(liste)
            if symbole == "!=":
                if liste[index_variable] not in liste_valeur:
                    new_data.append(liste)
            if symbole == "<":
                if float(liste[index_variable]) < float(liste_valeur[0]):
                    new_data.append(liste)
            if symbole == "<=":
                if float(liste[index_variable]) <= float(liste_valeur[0]):
                    new_data.append(liste)
            if symbole == ">":
                if float(liste[index_variable]) > float(liste_valeur[0]):
                    new_data.append(liste)
            if symbole == ">=":
                if float(liste[index_variable]) >= float(liste_valeur[0]):
                    new_data.append(liste)
            if symbole == "<>":
                if float(liste_valeur[0]) <= float(liste[index_variable]) <= float(liste_valeur[1]):
                    new_data.append(liste)
        return Jeu_de_donnees(new_data)
