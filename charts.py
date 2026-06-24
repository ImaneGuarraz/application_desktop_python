# charts.py

"""
Gère l'affichage des graphiques dans l'application
Contient plusieurs types de visualisations : simple, histogramme, top 10, pie chart
"""

import matplotlib
matplotlib.use("Agg")   # backend sans interface native

import matplotlib.pyplot as plt   # création du graphique
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg   # intégration Tkinter
import config   # couleurs Apple iOS


def show_chart_in_window(parent, rows):
    names = [row[1] for row in rows]   # extrait les noms
    values = [row[2] for row in rows]  # extrait les valeurs

    fig, ax = plt.subplots(figsize=(6, 3.5))   # taille du graphique

    fig.patch.set_facecolor(config.CARD_BG)   # fond de la card (verre clair)
    ax.set_facecolor("#ffffff")   # fond du graphique blanc pur

    ax.bar(
        names,
        values,
        color=config.ACCENT_COLOR,   # bleu Apple
        edgecolor="#d1d1d6"          # bordure gris clair
    )

    ax.set_title(
        "Graphique des valeurs",
        color=config.TEXT_COLOR,
        fontsize=14
    )   # titre Apple-like

    ax.tick_params(colors=config.TEXT_COLOR)   # couleur du texte des axes

    ax.spines["bottom"].set_color("#d1d1d6")   # bordure bas gris clair
    ax.spines["left"].set_color("#d1d1d6")     # bordure gauche gris clair
    ax.spines["top"].set_visible(False)        # supprime bordure haut
    ax.spines["right"].set_visible(False)      # supprime bordure droite

    canvas = FigureCanvasTkAgg(fig, master=parent)   # intègre matplotlib dans Tkinter
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)   # ajoute le graphique dans la card

