from gestion_scolaire.database.database import get_connection
from gestion_scolaire.models.eleve import Eleve
def ajouter_eleve(eleve: Eleve):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO eleves (matricule,nom,prenom,date_naissance,parent_id) VALUES (?,?,?,?,?)
    """,(
        eleve.matricule,
        eleve.nom,
        eleve.prenom,
        eleve.date_naissance,
        eleve.parent_id
    ))
    connection.commit()
    eleve.parent_id = cursor.lastrowid
    connection.close()
    return eleve