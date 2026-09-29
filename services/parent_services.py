from gestion_scolaire.database.database import get_connection
from gestion_scolaire.models.parent import Parent

def ajouter_parent(parent: Parent):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO parents(nom,telephone,email,adresse) VALUES (?, ?, ?,?)
    """, (parent.nom, parent.telephone, parent.email, parent.adresse))
    connection.commit()
    parent.id = cursor.lastrowid
    connection.close()
    return parent