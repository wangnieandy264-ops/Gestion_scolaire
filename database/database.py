import sqlite3
from pathlib import Path


# Chemin du dossier database
BASE_DIR = Path(__file__).resolve().parent

# Chemin de la base SQLite
DB_PATH = BASE_DIR / "school.db"


def get_connection():
    """Créer une connexion à la base de données."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialiser_base():
    """Créer les premières tables de la base de données."""

    connection = get_connection()
    cursor = connection.cursor()

    # Table école
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ecole (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL
        )
    """)

    # Table années scolaires
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS annees_scolaires (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            libelle TEXT NOT NULL UNIQUE,
            active INTEGER DEFAULT 0
        )
    """)

    # Table classes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS parents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL ,
    telephone TEXT NOT NULL ,
    email TEXT NOT NULL ,
    adresse TEXT NOT NULL )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleves(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricule TEXT NOT NULL UNIQUE,
    nom TEXT NOT NULL ,
    prenom TEXT NOT NULL ,
    date_naissance TEXT NOT NULL ,
    parent_id INTEGER NOT NULL ,
    FOREIGN KEY (parent_id) REFERENCES parents (id)
    )""")

    cursor.execute("""
    create TABLE IF NOT EXISTS inscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        eleve_id INTEGER NOT NULL ,
        annees_scolaires_id INTEGER NOT NULL ,
        classes_id INTEGER NOT NULL ,
        transport INTEGER DEFAULT 0,
        FOREIGN KEY (eleve_id) REFERENCES eleves (id),
        FOREIGN KEY (annees_scolaires_id) REFERENCES annees_scolaires (id),
        FOREIGN KEY (classes_id) REFERENCES classes (id),
        UNIQUE (eleve_id, annees_scolaires_id)
    )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialiser_base()
    print("Base de données initialisée avec succès.")
