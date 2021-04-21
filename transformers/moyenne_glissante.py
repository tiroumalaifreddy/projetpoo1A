class Moyenne_glissante:

    def __init__(self,data,n):
        self.data=data
        self.n=n

    def moyenne_glissante(self,data,n):

        liste_moyenne=[]
        for i in range(len(data)):
            liste=data[i:n+i]
            if len(self.liste)==n:
                somme=0
                for j in self.liste:
                    somme+=j[-1]
                liste_moyenne+=[round(somme/n,2)]
        return liste_moyenne

