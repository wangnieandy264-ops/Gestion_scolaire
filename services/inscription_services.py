from gestion_scolaire.models.inscription import Inscription
from gestion_scolaire.database.database import get_connection

def ajouter_inscription(inscription: Inscription):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into inscriptions (
    eleve_id,annees_scolaires_id,classes_id,transport
    ) values (?,?,?,?)""",(inscription.eleve_id,
                   inscription.annees_scolaires_id,
                   inscription.classes_id,
                   inscription.transport
                           ))
    connection.commit()
    inscription.id= cursor.lastrowid
    connection.close()
    return inscription

def recherche_inscription(inscription: Inscription):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT id ,eleve_id,annees_scolaires_id,classes_id,transport
                   FROM inscriptions
                   WHERE inscription.eleve_id=?
                   """,(inscription.eleve_id,))
    resultat = cursor.fetchone()
    connection.close()
    return resultat
def supprimer_inscription(inscription: Inscription):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    delete from inscriptions
    where eleve_id=?
    """,(inscription.eleve_id,))
    connection.commit()
    connection.close()
    return True