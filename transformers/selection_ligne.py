from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Selection_ligne(Transformers):
    def __init__(self, variable, liste_valeur, symbole = "="):
        self.variable = variable
        self.liste_valeur = liste_valeur
        self.symbole = symbole

    def transform(self, Table):
        index_variable = Table.column_names.index(self.variable)
        new_data = [Table.column_names]
        for liste in Table.rows:
            if self.symbole == "=":
                if liste[index_variable] in self.liste_valeur:
                    new_data.append(liste)
            if self.symbole == "!=":
                if liste[index_variable] not in self.liste_valeur:
                    new_data.append(liste)
            if self.symbole == "<":
                if float(liste[index_variable]) < float(self.liste_valeur[0]):
                    new_data.append(liste)
            if self.symbole == "<=":
                if float(liste[index_variable]) <= float(self.liste_valeur[0]):
                    new_data.append(liste)
            if self.symbole == ">":
                if float(liste[index_variable]) > float(self.liste_valeur[0]):
                    new_data.append(liste)
            if self.symbole == ">=":
                if float(liste[index_variable]) >= float(self.liste_valeur[0]):
                    new_data.append(liste)
            if self.symbole == "<>":
                if float(self.liste_valeur[0]) <= float(liste[index_variable]) <= float(self.liste_valeur[1]):
                    new_data.append(liste)
        return Jeu_de_donnees(new_data)