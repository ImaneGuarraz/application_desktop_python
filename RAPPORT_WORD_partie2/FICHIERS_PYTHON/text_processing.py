# text_processing.py

"""
Téléchargement et analyse du livre Frankenstein
"""

import re   # gère les expressions régulières
import math   # gère l'arrondi
from collections import Counter   # compte les occurrences
import requests   # télécharge le texte

FRANKENSTEIN_URL = "https://www.gutenberg.org/cache/epub/84/pg84.txt"   # URL du livre


def download_book(url: str = FRANKENSTEIN_URL) -> str:
    resp = requests.get(url, timeout=15)   # télécharge le texte brut
    resp.raise_for_status()   # lève une erreur si statut HTTP invalide
    return resp.text   # retourne le texte complet


def extract_metadata_and_first_chapter(text: str) -> dict:
    title_match = re.search(r"Title:\s*(.+)", text)   # extrait le titre
    author_match = re.search(r"Author:\s*(.+)", text)   # extrait l'auteur

    title = title_match.group(1).strip() if title_match else "Unknown title"   # nettoie le titre
    author = author_match.group(1).strip() if author_match else "Unknown author"   # nettoie l'auteur

    chapter_start = re.search(r"\bCHAPTER\s+I\b|\bCHAPTER\s+1\b", text)   # détecte début chapitre 1
    if not chapter_start:
        raise ValueError("Impossible de trouver le début du premier chapitre")   # erreur si absent

    start_idx = chapter_start.end()   # position après le titre du chapitre

    chapter_end = re.search(r"\nCHAPTER\s+II\b|\nCHAPTER\s+2\b", text[start_idx:])   # détecte chapitre 2
    if chapter_end:
        end_idx = start_idx + chapter_end.start()   # calcule la fin du chapitre 1
        first_chapter = text[start_idx:end_idx]   # extrait le chapitre
    else:
        first_chapter = text[start_idx:]   # prend tout si pas de chapitre 2

    return {
        "title": title,   # retourne le titre
        "author": author,   # retourne l'auteur
        "first_chapter": first_chapter.strip()   # retourne le chapitre nettoyé
    }


def paragraph_stats(chapter_text: str) -> dict:
    raw_paragraphs = [p.strip() for p in chapter_text.split("\n\n") if p.strip()]   # découpe en paragraphes

    word_counts = []   # liste des mots par paragraphe
    for p in raw_paragraphs:
        words = re.findall(r"\b\w+\b", p)   # détecte les mots
        word_counts.append(len(words))   # ajoute le nombre de mots

    rounded_counts = [int(math.floor(n / 10) * 10) for n in word_counts]   # arrondit à la dizaine
    distribution = Counter(rounded_counts)   # compte les occurrences

    stats = {
        "nb_paragraphs": len(raw_paragraphs),   # nombre total de paragraphes
        "total_words": sum(word_counts),   # total de mots
        "min_words": min(word_counts),   # paragraphe le plus court
        "max_words": max(word_counts),   # paragraphe le plus long
        "avg_words": sum(word_counts) / len(word_counts),   # moyenne
    }

    return {
        "raw_paragraphs": raw_paragraphs,   # liste brute
        "word_counts": word_counts,   # mots par paragraphe
        "rounded_counts": rounded_counts,   # arrondis
        "distribution": distribution,   # distribution
        "stats": stats   # statistiques globales
    }
