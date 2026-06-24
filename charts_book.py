# charts_book.py
"""
Graphique de distribution des longueurs de paragraphes
"""

import matplotlib
matplotlib.use("Agg")   # backend sans interface graphique

import matplotlib.pyplot as plt   # création du graphique


def create_paragraph_length_chart(distribution, output_path: str):
    lengths = sorted(distribution.keys())   # récupère les longueurs triées
    counts = [distribution[l] for l in lengths]   # récupère les fréquences

    fig, ax = plt.subplots(figsize=(7, 4))   # crée la figure

    ax.bar([str(l) for l in lengths], counts, color="#007aff", edgecolor="#1d1d1f")   # barres bleu Apple
    ax.set_xlabel("Longueur de paragraphe (arrondie)")   # label axe X
    ax.set_ylabel("Nombre de paragraphes")   # label axe Y
    ax.set_title('Distribution des longueurs — Frankenstein')   # titre

    plt.tight_layout()   # ajuste la mise en page
    fig.savefig(output_path, dpi=150)   # enregistre le graphique
    plt.close(fig)   # ferme la figure
