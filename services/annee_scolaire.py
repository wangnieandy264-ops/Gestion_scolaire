from  gestion_scolaire.models.annee_scolaire import AnneeSscolaire
from gestion_scolaire.database.database import get_connection

def ajouter_annee_scolaire(annee:AnneeSscolaire):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into annees_scolaires (libelle,active) values (?,?)
    """,(
        annee.libelle,
        annee.active,
    ))
    connection.commit()
    annee.id = cursor.lastrowid
    connection.close()
    return annee