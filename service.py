# service.py

"""
Ce fichier gère l'importation des données depuis un fichier local ou depuis une URL. 
il utilise l'importeur universel pour lire n'importe quel format (json, csv, txt, docx, xlsx)"""

import requests
import tempfile

from universal_importer import extract_data_any_format
from database import insert_item


# importation depuis un fichier local
def import_from_file(path):
    # extrait les données sous forme (name, value)
    items = extract_data_any_format(path)

    # insère chaque élément dans sqlite
    for name, value in items:
        insert_item(name, value)


# importation depuis une URL
def import_from_url(url):
    # télécharge le contenu de l'url
    response = requests.get(url)
    response.raise_for_status()

    # crée un fichier temporaire pour stocker le contenu
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name

    # extrait les données depuis le fichier temporaire
    items = extract_data_any_format(tmp_path)

    # insère dans sqlite
    for name, value in items:
        insert_item(name, value)
