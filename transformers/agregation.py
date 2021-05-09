from transformers.transformers import Transformers
from Data.Jeu_de_donnees import Jeu_de_donnees

class Agregation(Transformers):
    def __init__(self, index_variable_agr, variable_modifie, echelle):
        self.index_variable_agr = index_variable_agr
        self.variable_modifie = variable_modifie
        self.echelle = echelle

    def transform(self, Table):
        liste_dep_reg = [['departmentCode', 'regionCode'], ['01', '84'], ['02', '32'], ['03', '84'], ['04', '93'], ['05', '93'], ['06', '93'], ['07', '84'], ['08', '44'], ['09', '76'], ['1', '84'], ['2', '32'], ['3', '84'], ['4', '93'], ['5', '93'], ['6', '93'], ['7', '84'], ['8', '44'], ['9', '76'],['10', '44'], ['11', '76'], ['12', '76'], ['13', '93'], ['14', '28'], ['15', '84'], ['16', '75'], ['17', '75'], ['18', '24'], ['19', '75'], ['21', '27'], ['22', '53'], ['23', '75'], ['24', '75'], ['25', '27'], ['26', '84'], ['27', '28'], ['28', '24'], ['29', '53'], ['2A', '94'], ['2B', '94'], ['2a', '94'], ['2b', '94'], ['30', '76'], ['31', '76'], ['32', '76'], ['33', '75'], ['34', '76'], ['35', '53'], ['36', '24'], ['37', '24'], ['38', '84'], ['39', '27'], ['40', '75'], ['41', '24'], ['42', '84'], ['43', '84'], ['44', '52'], ['45', '24'], ['46', '76'], ['47', '75'], ['48', '76'], ['49', '52'], ['50', '28'], ['51', '44'], ['52', '44'], ['53', '52'], ['54', '44'], ['55', '44'], ['56', '53'], ['57', '44'], ['58', '27'], ['59', '32'], ['60', '32'], ['61', '28'], ['62', '32'], ['63', '84'], ['64', '75'], ['65', '76'], ['66', '76'], ['67', '44'], ['68', '44'], ['69', '84'], ['70', '27'], ['71', '27'], ['72', '52'], ['73', '84'], ['74', '84'], ['75', '11'], ['76', '28'], ['77', '11'], ['78', '11'], ['79', '75'], ['80', '32'], ['81', '76'], ['82', '76'], ['83', '93'], ['84', '93'], ['85', '52'], ['86', '75'], ['87', '75'], ['88', '44'], ['89', '27'], ['90', '27'], ['91', '11'], ['92', '11'], ['93', '11'], ['94', '11'], ['95', '11'], ['971', '01'], ['972', '02'], ['973', '03'], ['974', '04'], ['976', '06'], ['971', '1'], ['972', '2'], ['973', '3'], ['974', '4'], ['976', '6']]
        liste_reg = ['01', '02', '03', '04', '06', '11', '24', '27', '28', '32', '44', '52', '53', '75', '76', '84', '93', '94']
        if self.echelle == "nationale":
            new_data = [[self.variable_modifie]]
            somme = 0
            for liste in Table.rows:
                somme += float(liste[Table.column_names.index(self.variable_modifie)])
            new_data.append([somme])
        if self.echelle == "region":
            data_imp = [['numRegion', self.variable_modifie]]
            for numRegion in liste_reg:
                liste = []
                for k in liste_dep_reg[1:]:
                    if k[1] == numRegion:
                        liste.append(k[0])
                liste_deux = []
                for i in Table.rows:
                    if i[self.index_variable_agr] in liste:
                        liste_deux.append(i)
                somme = 0
                for k in liste_deux:
                    somme += float(k[Table.column_names.index(self.variable_modifie)])
                data_imp.append([numRegion, somme])
        return Jeu_de_donnees(data_imp)

            
