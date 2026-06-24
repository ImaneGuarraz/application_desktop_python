# Projet : Application Desktop d’Analyse de Données (Tkinter)

#### Auteur : 
👩🏽‍💻 Imane

#### Date : 
📅 24 juin 2026

---

## Application Desktop d’Analyse de Données

Création d'une application desktop avec l'utilisation du module Python Tkinter. L'application stocke les données téléchargées depuis Internet dans la base de données et afficher des résumés des données téléchargées et leur représentation graphique.

Le but est que l'utilisateur puisse télécharger un fichier (CSS, Word, txt, ...) ou un lien JSON, dans l'application et que cela génère un résumé chiffré et visuel de ces données d'entrée. 

--- 

## Vue d’ensemble du projet

L'application va permettre de :

- Télécharger des données JSON depuis Internet
- Les stocker dans une base SQLite (app_desktop_python.db)
- Afficher des résumés (agrégations SQL)
- Afficher des graphiques dans une fenêtre Tkinter
- Proposer un menu pour :
  - effacer la base
  - télécharger les données
  - changer des options (couleurs, polices…)

---

## Structure du projet 

partie2/
│
├── text_processing.py      # téléchargement + extraction + analyse du texte
├── image_processing.py     # téléchargement + recadrage + collage des images
├── charts_book.py          # génération du graphique
├── report_word.py          # génération du document Word
├── partie2_main.py         # script principal orchestrateur
└── assets/
      └── logo.png          # image #2 (logo noir et blanc)
