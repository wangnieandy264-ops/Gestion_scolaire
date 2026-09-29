from gestion_scolaire.models.eleve import Eleve
from gestion_scolaire.services.eleve_service import ajouter_eleve

eleve = Eleve(
    "wangnie",
    "dupont",
    "ELV003",
    1,
"2012-05-10",
    2
)
eleve=ajouter_eleve(eleve)
print("eleve enregistree")
print("id:",eleve.id)
print("parent_id:",eleve.parent_id)
print("nom complet: ",eleve.nom_complet())