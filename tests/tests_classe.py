from gestion_scolaire.models.classe import Classe
from gestion_scolaire.services.classe_service import ajouter_classe

classe = Classe(
    "6EME",
    1
)
print("classe enregistre")
print("classe id",classe.id)
print("nom",classe.nom)