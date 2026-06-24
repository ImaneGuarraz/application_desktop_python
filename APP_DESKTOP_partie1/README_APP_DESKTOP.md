# 🖥️ Projet : Application Desktop d’Analyse de Données (Tkinter)

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

Python_App_Desktop/  
│  
├── main.py 
├── universal_importer.py  
├── service.py  
├── database.py                 
├── charts.py              
├── config.py      
├── README.md     
└── app_desktop_python.db (se créer une fois l'application lancée)


> main.py : Fenêtre Tkinter + menus + boutons
> universal_importer.py : lecture de divers fichiers (JSON, CSV, TXT, DOCX, XLSX)
> database.py : Connexion SQLite + CRUD
> chart.py : Graphiques matplotlib
> config.py : Options (couleurs, polices…)
> Readme : documentation 
> app_desktop_python.db : Base SQLite (créée automatiquement)  

---

## Les outils 

<p align="left">
  <img src="https://img.shields.io/badge/VS%20Code-2EC4B6?style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-6CA0DC?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-386641?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-F4D35E?style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/badge/Matplotlib-9D4EDD?style=for-the-badge&logo=plotly&logoColor=white"/>
</p>

---

## Fonctionnalités principales

### Importation universelle
    - Fichiers : CSV, TXT, JSON, DOCX, XLSX
    - URL : téléchargement et parsing automatique

### Stockage local
    - Base SQLite intégrée
    - Nettoyage complet de la base

### Analyse automatique
    - Somme des valeurs
    - Moyenne des valeurs

### Visualisation
    - Graphique intégré (matplotlib)
    - Style moderne iOS Light avec “cards”

### Interface moderne
    - Sidebar 
    - Boutons arrondis
    - Cards “verre très clair” pour les résultats

### Gestion d’erreurs 
    - Popup d’erreur
    - Messages d’état
    - Vérification des données avant analyse

---

## Installation en local

> Attention : si vous êtes sur Mac il faut télécharger la version Python3.12 et lui donner l'accès dans les réglages système, car c'est la dernière version avec Tkinter accessible. 

1. Cloner 
`git clone https://github.com/<ton-repo>/analyse-donnees-tkinter.git
cd analyse-donnees-tkinter`

2. Installer les dépendances
`pip install -r requirements.txt`

3. Lancer l’application
`python3 main.py`

---

## Guide d’utilisation

1. Lancer l’application
Une fenêtre Tkinter s’ouvre avec :
- un menu latéral
- une zone centrale affichant les résultats

2. Importer un document
- Cliquer sur Importer un document
- Choisir un fichier parmi : .csv, .txt, .json, .docx, .xlsx
- Le fichier est automatiquement : lu, converti et inséré dans la base SQLite
- Un message de confirmation apparaît dans une card iOS.

3. Importer depuis une URL
- Cliquer sur Importer depuis une URL
- Entrer une URL valide
- Les données sont téléchargées et stockées dans la base

4. Analyser le document
- Cliquer sur Analyser le document
- L’application affiche :
    - une card “Agrégations”
    - une card “Graphiques”
- Les calculs effectués :
    - Somme des valeurs
    - Moyenne des valeurs
    - Graphique des valeurs

5. Effacer la base
- Cliquer sur Effacer la base
- Confirmation demandée
- La base SQLite est vidée

---

## Gestion des erreurs

L’application gère :
- fichiers invalides
- URL incorrectes
- absence de données
- erreurs réseau
- erreurs SQLite
- erreurs de parsing

> ⚠️ Chaque erreur déclenche une popup explicite.

## Tests unitaires

Les modules pouvant être testés :

- service.import_from_file
- service.import_from_url
- database.aggregate_sum
- database.aggregate_avg
- charts.show_chart_in_window (testable via backend Agg)

## Limites actuelles

Tkinter ne permet pas un style aussi moderne qu’une app web
- Pas de responsive
- Pas de thèmes dynamiques
- Importation limitée à certains formats

