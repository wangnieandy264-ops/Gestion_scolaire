from gestion_scolaire.models.parent import Parent
from gestion_scolaire.services.parent_services import ajouter_parent
parent = Parent(
        "jean",
        "651651661",
        "fsrgsef@gmail.com",
        "gvdfvsfsd"
    )
print("Nom:",parent.nom)
print("Adresse:",parent.adresse)
print("telephone:",parent.telephone)
print("email:",parent.email)
parent = ajouter_parent(parent)
print("parent enregistre avec succes")
print("ID:",parent.id)
print("nom:",parent.nom)


