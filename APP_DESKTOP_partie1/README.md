# PROJET PYTHON AVANCÉ 

---

## PARTIE 1 : Application Desktop Python

Création d'une application desktop avec l'utilisation du module Python Tkinter. L'application stocke les données téléchargées depuis Internet dans la base de données et afficher des résumés des données téléchargées et leur représentation graphique.

Le but est que l'utilisateur puisse télécharger un fichier (CSS, Word, txt, ...) ou un lien JSON, dans l'application et que cela génère un résumé chiffré et visuel de ces données d'entrée. 


# TO DO 
- [x] Partie 1
- [ ] Partie 2 
- [ ] Github
- [ ] ReadMe
- [ ] Requierements
- [ ] Vidéo de présentation de tout 




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


## Structure du projet 

Python_App_Desktop/  
│  
├── main.py 
├── universal_importer.py  
├── service.py  
├── database.py                 
├── charts.py              
├── config.py              
└── app_desktop_python.db 

> main.py : Fenêtre Tkinter + menus + boutons
> database.py : Connexion SQLite + CRUD
> chart.py : Graphiques matplotlib
> config.py : Options (couleurs, polices…)
> app_desktop_python.db : Base SQLite (créée automatiquement)  

"""
universal_importer.py
---------------------

Rôle du fichier :
Ce module fournit un importeur UNIVERSEL capable de lire presque tous les formats
de fichiers utilisés dans ton application : JSON, CSV, TXT, DOCX, XLSX.




## Les outils 

<p align="left">
  <img src="https://img.shields.io/badge/VS%20Code-2EC4B6?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-6CA0DC?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-386641?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-F4D35E?style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/badge/Matplotlib-9D4EDD?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>


Ton fichier database.py contient toute la logique SQLite :

Fonction	Rôle
get_connection	ouvrir la base
create_table	créer la table
insert_item	insérer une ligne
get_all_items	lire toutes les données
get_average_size	calculer une moyenne
clear_database	vider la base
is_database_empty	vérifier si la base est vide

## Ce que l'application fait : 

Et dans ton app Tkinter :
Afficher statistiques → OK

Graphique simple → OK

Histogramme → OK

Top 10 → OK

Pie chart → OK

Tu vas voir des choses comme :

Top 10 des astéroïdes les plus gros

Répartition safe / hazardous

Histogramme des tailles

Courbe des distances

## Mise en forme app



## Lancement de l'application : 

> Attention : si vous êtes sur Mac il faut télécharger la version Python3.12 et lui donner l'accès dans les réglages système, car c'est la dernière version avec Tkinter accessible. 


### Ouvrez votre terminal et taper les commandes suivantes :

- Se rendre sur le bon dossier : `cd "votre chemin"`

- Vérifier que vous soyez sur la bonne version Python : `python3.12 --version`
  
- mise à jour de Pip `python3.12 -m pip install --upgrade pip`
  
- installer les dépendances nécessaires :
  - `python3.12 -m pip install requests`
  - `python3.12 -m pip install matplotlib`
  - `python3.12 -m pip install pandas`
 
- tester l'ouverture de Tkinter 
  - Si vous avez déjà Tkinter : 
    `python3.12 - << 'EOF'
    import tkinter as tk
    root = tk.Tk()
    root.mainloop()
    EOF`
  - Si vous n'avez pas Tkinter : 
    - `brew install python-tk@3.11`
    - `brew install tcl-tk`
    - `brew install python@3.11 --with-tcl-tk`

- Lancement de l'application : `python3 main.py`




