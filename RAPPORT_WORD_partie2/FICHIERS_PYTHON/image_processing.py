# image_processing.py

"""
Téléchargement et traitement des images pour le rapport Frankenstein
"""

import requests   # télécharge l'image
from PIL import Image   # gère les images
from io import BytesIO   # convertit les données binaires


def download_image(url: str, output_path: str):
    resp = requests.get(url, timeout=15)   # télécharge l'image
    resp.raise_for_status()   # vérifie le statut HTTP
    img = Image.open(BytesIO(resp.content))   # ouvre l'image en mémoire
    img.save(output_path)   # enregistre l'image sur disque
    return output_path   # retourne le chemin


def process_images(image1_path: str, logo_path: str, output_path: str):
    img1 = Image.open(image1_path).convert("RGB")   # ouvre image #1
    img1 = img1.resize((900, 600))   # redimensionne l'image principale

    w, h = img1.size   # récupère dimensions
    crop_box = (0, 0, w, int(h * 0.85))   # recadre légèrement en hauteur
    img1 = img1.crop(crop_box)   # applique le recadrage

    logo = Image.open(logo_path).convert("L")   # ouvre logo en noir et blanc
    logo = logo.rotate(25, expand=True)   # pivote le logo
    logo = logo.resize((180, 180))   # redimensionne le logo

    pos_x = w - logo.width - 20   # position X du logo
    pos_y = h - logo.height - 20   # position Y du logo

    img1.paste(logo, (pos_x, pos_y), mask=logo)   # colle le logo avec transparence
    img1.save(output_path)   # enregistre l'image finale

    return output_path   # retourne le chemin final
