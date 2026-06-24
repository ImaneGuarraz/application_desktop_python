# main.py

"""
script principal orchestrant toutes les étapes du pipeline
"""

from text_processing import download_book, extract_metadata_and_first_chapter, paragraph_stats  # importe les fonctions de traitement texte
from charts_book import create_paragraph_length_chart  # importe la fonction de création du graphique
from image_processing import process_images  # importe la fonction de traitement d'image
from report_word import create_report_docx  # importe la fonction de génération du document word

# définit le chemin de l'image locale utilisée comme image #1
IMAGE1_LOCAL = "assets/frankenstein_local.jpg"  # indique l'image locale


def main():
    try:
        print("Téléchargement du livre...")
        text = download_book()  # télécharge le texte brut du livre

        print("Extraction du chapitre 1...")
        meta = extract_metadata_and_first_chapter(text)  # extrait titre, auteur et premier chapitre
        chapter = meta["first_chapter"]  # récupère le chapitre extrait

        print("Analyse des paragraphes...")
        analysis = paragraph_stats(chapter)  # calcule les statistiques des paragraphes
        stats = analysis["stats"]  # récupère les statistiques globales

        print("Création du graphique...")
        chart_path = "frankenstein_distribution.png"  # définit le nom du fichier graphique
        create_paragraph_length_chart(analysis["distribution"], chart_path)  # génère le graphique

        print("Utilisation de l'image locale #1...")
        img1_path = IMAGE1_LOCAL  # définit le chemin de l'image locale

        print("Traitement des images...")
        final_image_path = process_images(img1_path, "assets/logo.png", "image_finale.jpg")  # traite l'image et colle le logo

        print("Création du document Word...")
        output_docx = create_report_docx(meta, stats, chart_path, final_image_path, "Rapport_Frankenstein.docx")  # génère le document word

        print("\n=== Rapport généré ===")
        print(f"Document Word : {output_docx}")  # affiche le chemin du document généré
        print(f"Graphique : {chart_path}")  # affiche le chemin du graphique
        print(f"Image finale : {final_image_path}")  # affiche le chemin de l'image finale

    except Exception as e:
        print("\n❌ Une erreur est survenue :")
        print(str(e))  # affiche l'erreur rencontrée


if __name__ == "__main__":
    main()  # exécute la fonction principale

