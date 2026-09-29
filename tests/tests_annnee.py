from gestion_scolaire.models.annee_scolaire import AnneeSscolaire
from gestion_scolaire.services.annee_scolaire import ajouter_annee_scolaire
annee_scolaire = AnneeSscolaire(
    "2027-2028",
    active=True,
)
annee_scolaire = ajouter_annee_scolaire(annee_scolaire)
print("annees ajouter ")
print("id",annee_scolaire.id)
print("libelle",annee_scolaire.libelle)
print("active:",annee_scolaire.active)