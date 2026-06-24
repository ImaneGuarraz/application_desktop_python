# test_text_processing.py

"""
Tests unitaires pour la partie 2
"""

import pytest   # framework de tests
from text_processing import extract_metadata_and_first_chapter, paragraph_stats


def test_extract_metadata_and_first_chapter():
    fake_text = (
        "Title: Frankenstein\n"
        "Author: Mary Shelley\n\n"
        "CHAPTER I\n"
        "This is a test paragraph.\n\n"
        "CHAPTER II\n"
    )   # texte factice

    meta = extract_metadata_and_first_chapter(fake_text)   # extraction

    assert meta["title"] == "Frankenstein"   # vérifie titre
    assert meta["author"] == "Mary Shelley"   # vérifie auteur
    assert "This is a test paragraph" in meta["first_chapter"]   # vérifie contenu


def test_paragraph_stats():
    chapter = (
        "First paragraph with ten words exactly here now.\n\n"
        "Second paragraph with more words than the first one indeed.\n"
    )   # chapitre factice

    result = paragraph_stats(chapter)   # analyse

    assert result["stats"]["nb_paragraphs"] == 2   # 2 paragraphes
    assert result["stats"]["min_words"] > 0   # min > 0
    assert result["stats"]["max_words"] >= result["stats"]["min_words"]   # max >= min
    assert len(result["rounded_counts"]) == 2   # 2 arrondis
