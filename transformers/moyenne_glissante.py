from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers
from transformers.jointure_vertical import Jointure_vertical

class Moyenne_glissante(Transformers):

    # def __init__(self,data,n):
    #     self.data=data
    #     self.n=n

    # def moyenne_glissante(self,data,n,variable):
    #
    #     liste_moyenne=[]
    #     indice_variable = data[0].index(variable)
    #     for i in range(1, len(data)):
    #         liste=data[i:n+i]
    #         if len(liste)==n:
    #             somme=0
    #             for j in liste:
    #                 somme+=int(j[indice_variable])
    #                 liste_moyenne+=[round(somme/n,2)]
    #     return liste_moyenne

    def transform(self,Table, n, variable):
        liste_moyenne = []
        indice_variable = Table.column_names.index(variable)
        for i in range(len(Table.rows)):
            liste = Table.rows[i:n + i]
            if len(liste) == n:
                somme = 0
                for j in liste:
                    somme += float(j[indice_variable])
                liste_moyenne += [[round(somme / n, 2)]]
        new_column = [["M_glissante n{} de {}".format(n,variable)]] + liste_moyenne
        new_Table = Jeu_de_donnees(new_column)
        return Jointure_vertical().transform(Table, new_Table)
