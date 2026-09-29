from gestion_scolaire.database.database import get_connection
from gestion_scolaire.models.classe import Classe

def ajouter_classe (classe:Classe):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into classes (nom) values (?)""",
                   (classe.nom,))
    connection.commit()
    classe.id = cursor.lastrowid
    connection.close()
    return classe