# database.py

"""
Ce fichier gère la base sqlite : création de la table, insertion, suppression, récupération et agrégations."""

import sqlite3

DB_NAME = "app_desktop_python.db"

# connexion sqlite
def get_connection():
    return sqlite3.connect(DB_NAME)


# création de la table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL
        )
    """)

    conn.commit()
    conn.close()


# insertion d'un élément
def insert_item(name, value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO items (name, value) VALUES (?, ?)", (name, value))

    conn.commit()
    conn.close()


# suppression de toutes les données
def clear_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM items")

    conn.commit()
    conn.close()


# récupération de toutes les lignes
def get_all_items():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, value FROM items")
    rows = cursor.fetchall()

    conn.close()
    return rows


# vérifie si la base est vide
def is_database_empty():
    return len(get_all_items()) == 0


# agrégations
def aggregate_sum():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(value) FROM items")
    result = cursor.fetchone()[0]

    conn.close()
    return result or 0

# agrégations
def aggregate_avg():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(value) FROM items")
    result = cursor.fetchone()[0]

    conn.close()
    return result or 0
