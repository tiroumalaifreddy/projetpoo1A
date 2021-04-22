class Moyenne_glissante:

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

    def moyenne_glissante(self,data, n, variable):
        liste_moyenne = []
        indice_variable = data[0].index(variable)
        for i in range(1, len(data)):
            liste = data[i:n + i]
            if len(liste) == n:
                somme = 0
                for j in liste:
                    somme += float(j[indice_variable])
                liste_moyenne += [round(somme / n, 2)]
        return liste_moyenne
