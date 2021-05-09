from Data.Jeu_de_donnees import Jeu_de_donnees
from estimators.ecart_type import Ecart_type
from estimators.kmeans import Kmeans
from estimators.moyenne import Moyenne
from transformers.agregation import Agregation
from transformers.centrage import Centrage
from transformers.clean import Clean
from transformers.conversion import Conversion
from transformers.fenetrage import Fenetrage
from transformers.jointure_vertical import Jointure_vertical
from transformers.moyenne_glissante import Moyenne_glissante
from transformers.normalisation import Normalisation
from transformers.selection_ligne import Selection_ligne
from transformers.selection_variable import Selection_variable
from transformers.total_id import Total_id
from transformers.transformers import Transformers

class Pipeline(Transformers):
    def transform(self, Table, liste_operation):
        for operation in liste_operation:
            Table = operation.transform(Table)
        return Table
