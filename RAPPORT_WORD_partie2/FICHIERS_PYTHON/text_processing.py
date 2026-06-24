# text_processing.py

"""
module chargé de :
- lire le livre en local
- extraire le titre, l'auteur et le chapitre 1
- analyser les paragraphes
"""

import re  # importe regex pour analyser le texte
from collections import Counter  # importe counter pour compter les mots


def download_book():
    # lit le livre en local pour éviter les erreurs réseau
    with open("assets/pg84.txt", "r", encoding="utf-8") as f:  # ouvre le fichier texte local
        return f.read()  # retourne le contenu du livre


def extract_metadata_and_first_chapter(text: str):
    # extrait le titre du livre
    title_match = re.search(r"Title:\s*(.*)", text)  # cherche la ligne du titre
    title = title_match.group(1).strip() if title_match else "Titre inconnu"  # récupère le titre

    # extrait l'auteur du livre
    author_match = re.search(r"Author:\s*(.*)", text)  # cherche la ligne de l'auteur
    author = author_match.group(1).strip() if author_match else "Auteur inconnu"  # récupère l'auteur

    # extrait le chapitre 1
    chapter_match = re.search(
    r"(CHAPTER\s+I|Chapter\s+I|CHAPTER\s+1|Chapter\s+1|CHAPTER\s+One|Chapter\s+One)\s*(.*?)(CHAPTER\s+II|Chapter\s+II|CHAPTER\s+2|Chapter\s+2|CHAPTER\s+Two|Chapter\s+Two|$)",
    text,
    re.DOTALL
    ) # isole le chapitre 1
    
    chapter = chapter_match.group(1).strip() if chapter_match else ""  # récupère le texte du chapitre

    # retourne les informations extraites
    return {
        "title": title,  # stocke le titre
        "author": author,  # stocke l'auteur
        "first_chapter": chapter  # stocke le chapitre 1
    }


def paragraph_stats(chapter_text: str):
    # découpe le chapitre en paragraphes
    paragraphs = [p.strip() for p in chapter_text.split("\n\n") if p.strip()]  # isole les paragraphes

    # calcule le nombre de mots par paragraphe
    lengths = [len(p.split()) for p in paragraphs]  # compte les mots dans chaque paragraphe

    # arrondit les longueurs à la dizaine
    rounded = [((n // 10) * 10) for n in lengths]  # arrondit à la dizaine inférieure

    # construit la distribution
    distribution = Counter(rounded)  # compte combien de paragraphes par tranche de mots

    # calcule les statistiques globales
    stats = {
        "nb_paragraphs": len(paragraphs),  # nombre total de paragraphes
        "total_words": sum(lengths),  # total de mots
        "min_words": min(lengths) if lengths else 0,  # minimum
        "max_words": max(lengths) if lengths else 0,  # maximum
        "avg_words": sum(lengths) / len(lengths) if lengths else 0  # moyenne
    }

    # retourne les résultats
    return {
        "distribution": distribution,  # distribution des paragraphes
        "stats": stats  # statistiques globales
    }
