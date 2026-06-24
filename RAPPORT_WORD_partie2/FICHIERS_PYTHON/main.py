# main.py

"""
Script principal complet de la partie 2 avec gestion d'erreurs
"""

from text_processing import download_book, extract_metadata_and_first_chapter, paragraph_stats
from charts_book import create_paragraph_length_chart
from image_processing import download_image, process_images
from report_word import create_report_docx


IMAGE1_URL = "https://upload.wikimedia.org/wikipedia/commons/3/35/Frankenstein%27s_monster_%281931%29.jpg"   # image #1


def main():
    try:
        print("Téléchargement du livre...")   # info
        text = download_book()   # télécharge Frankenstein

        print("Extraction du chapitre 1...")   # info
        meta = extract_metadata_and_first_chapter(text)   # extrait infos
        chapter = meta["first_chapter"]   # récupère chapitre

        print("Analyse des paragraphes...")   # info
        analysis = paragraph_stats(chapter)   # calcule stats
        stats = analysis["stats"]   # stats globales

        print("Création du graphique...")   # info
        chart_path = "frankenstein_distribution.png"   # chemin graphique
        create_paragraph_length_chart(analysis["distribution"], chart_path)   # génère graphique

        print("Téléchargement de l'image #1...")   # info
        img1_path = download_image(IMAGE1_URL, "image1.jpg")   # télécharge image

        print("Traitement des images...")   # info
        final_image_path = process_images(img1_path, "assets/logo.png", "image_finale.jpg")   # traite images

        print("Création du document Word...")   # info
        output_docx = create_report_docx(meta, stats, chart_path, final_image_path, "Rapport_Frankenstein.docx")   # génère Word

        print("\n=== Rapport généré ===")   # résumé
        print(f"Document Word : {output_docx}")   # chemin Word
        print(f"Graphique : {chart_path}")   # chemin graphique
        print(f"Image finale : {final_image_path}")   # chemin image

    except Exception as e:
        print("\n❌ Une erreur est survenue :")   # message erreur
        print(str(e))   # affiche l'erreur


if __name__ == "__main__":
    main()   # lance le script
