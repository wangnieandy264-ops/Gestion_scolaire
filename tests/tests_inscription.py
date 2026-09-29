from gestion_scolaire.models.inscription import Inscription
from gestion_scolaire.services.inscription_services import recherche_inscription ,ajouter_inscription ,supprimer_inscription
def test_ajout_supprimer_inscription():
    inscription =Inscription(
        None,
        2,
        3,
        1,
        True
                             )
    inscription = ajouter_inscription(inscription)
    assert inscription.id is not None
    resultat = recherche_inscription(inscription)
    assert resultat is not None
    assert resultat[1] == inscription.eleve_id
    print("eleve trouvee")
    supprimer_inscription(inscription)
    resultat_apres = recherche_inscription(inscription)
    assert resultat_apres is not None
    print("inscription supprimer")
