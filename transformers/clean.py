from Data.Jeu_de_donnees import Jeu_de_donnees
from transformers.transformers import Transformers


class Clean(Transformers):
    def transform(self, Table, remove=False):
        if not remove:
            indice = 0
            for liste in Table.rows:
                for i in liste:
                    if str(i).lower() in ["none", "null", "na"]:
                        indice = 1
            if indice == 1:
                print("Des valeurs sont manquantes")
            if indice == 0:
                print("Aucune valeur manquante")
        if remove:
            new_data=[Table.column_names]
            for liste in Table.rows:
                indice = 0
                for i in liste:
                    if str(i).lower()  in ["none", "null", "na"]:
                        indice = 1
                if indice == 0:
                    new_data.append(liste)
            return Jeu_de_donnees(new_data)

