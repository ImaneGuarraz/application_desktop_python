# Projet : Analyse d’un Livre & Génération Automatique d’un Rapport Word

#### Auteur :  
👩🏽‍💻 Imane

#### Date :  
📅 24 juin 2026

---

## Analyse d’un Livre & Génération d’un Rapport Word

Création d’un programme Python permettant de télécharger un livre depuis **Project Gutenberg**, d’en extraire automatiquement les informations essentielles (titre, auteur, premier chapitre), d’analyser le contenu textuel, de générer un graphique statistique, de traiter des images, puis de produire un **document Word complet** contenant :

- une page de titre  
- une image traitée  
- un graphique personnalisé  
- une description détaillée du chapitre analysé  

Ce projet met en œuvre :  
✔ traitement de texte  
✔ analyse statistique  
✔ manipulation d’images  
✔ génération de documents Word  
✔ gestion d’erreurs  
✔ tests unitaires  

---

## Vue d’ensemble du projet

Le programme permet de :

- Télécharger automatiquement un livre depuis **Project Gutenberg**
- Extraire :
  - le titre du livre  
  - le nom de l’auteur  
  - le premier chapitre  
- Analyser le premier chapitre :
  - découpe en paragraphes  
  - comptage des mots  
  - arrondi à la dizaine  
  - distribution statistique  
- Générer un graphique de distribution  
- Télécharger une image #1 depuis Internet  
- Recadrer et redimensionner l’image  
- Lire un logo #2 depuis le disque, le pivoter et le coller sur l’image #1  
- Générer un **document Word complet** contenant :
    - page de titre  
    - image traitée  
    - graphique  
    - résumé d’intrigue  
    - statistiques détaillées  

---

## Structure du projet

Partie2/  
│  
├── text_processing.py  
├── image_processing.py  
├── charts_book.py  
├── report_word.py  
├── partie2_main.py  
├── assets/  
│   └── logo.png  
└── README.md  

> text_processing.py : téléchargement du livre + extraction du chapitre + analyse textuelle  
> image_processing.py : téléchargement, recadrage, redimensionnement, collage du logo  
> charts_book.py : création du graphique de distribution  
> report_word.py : génération du document Word complet  
> partie2_main.py : script principal orchestrant toutes les étapes  
> assets/logo.png : logo noir et blanc utilisé pour le collage  
> README.md : documentation du projet  

---

## Les outils

<p align="left">
  <img src="https://img.shields.io/badge/Python-6CA0DC?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Requests-386641?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-9D4EDD?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pillow-F4D35E?style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/badge/python--docx-2EC4B6?style=for-the-badge&logo=microsoftword&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pytest-FF6B6B?style=for-the-badge&logo=pytest&logoColor=white"/>
</p>

---

## Fonctionnalités principales

### Téléchargement du livre
    - Récupération automatique du texte brut depuis Project Gutenberg  
    - Extraction du titre, de l’auteur et du premier chapitre  

### Analyse textuelle
    - Découpage en paragraphes  
    - Comptage du nombre de mots  
    - Arrondi à la dizaine  
    - Distribution statistique  
    - Calcul des valeurs min / max / moyenne  

### Graphique personnalisé
    - Création d’un graphique de distribution  
    - Sauvegarde en PNG  
    - Intégration dans le document Word  

### Traitement d’images
    - Téléchargement d’une image #1 depuis Internet  
    - Recadrage et redimensionnement  
    - Lecture d’un logo noir et blanc  
    - Rotation du logo  
    - Collage du logo sur l’image #1  

### Génération du document Word
    - Page de titre avec :
      - titre du livre  
      - auteur  
      - auteur du rapport  
      - image traitée  
      
    - Page graphique avec :
      - graphique  
      - résumé d’intrigue  
      - statistiques détaillées  
      - source des données  

### Gestion d’erreurs
    - Téléchargement impossible  
    - Livre introuvable  
    - Chapitre non détecté  
    - Image inaccessible  
    - Fichier Word non générable  

### Tests unitaires
    - Extraction du chapitre  
    - Analyse des paragraphes  
    - Distribution des longueurs  

---

## Installation en local

1. Cloner le projet  
`bash
git clone https://github.com/<ton-repo>/analyse-livre-frankenstein.git
cd analyse-livre-frankenstein`

2. Installer les dépendances
`pip install -r requirements.txt`

3. Lancer le stript principal
`python3 main.py`

---

## Guide d’utilisation

1. Le script télécharge automatiquement le livre **Frankenstein** depuis Project Gutenberg  
2. Il extrait :
     
       - le titre du livre  
       - le nom de l’auteur  
       - le premier chapitre
  
4. Il analyse le premier chapitre :
   
       - découpe en paragraphes  
       - comptage du nombre de mots  
       - arrondi à la dizaine  
       - création d’une distribution statistique
  
6. Il génère un graphique PNG représentant la distribution des longueurs de paragraphes

7. Il télécharge une image #1 depuis Internet  

8. Il lit un logo #2 depuis le disque, le pivote et le colle sur l’image #1  

9. Il génère un document Word contenant :

       - une page de titre  
       - l’image traitée  
       - le graphique  
       - un résumé d’intrigue  
       - les statistiques détaillées du chapitre  
   
10. Le fichier final est généré sous le nom :  
   **📄 Rapport_Frankenstein.docx**

---

## Gestion des erreurs

Le programme gère :

- erreurs réseau lors du téléchargement du livre ou de l’image  
- livre introuvable ou format inattendu  
- chapitre non détecté  
- image #1 inaccessible  
- logo manquant ou illisible  
- erreur lors de la génération du graphique  
- erreur lors de la création du document Word  

> En cas d’erreur, un message clair est affiché dans la console pour éviter l’arrêt brutal du programme.

## Tests unitaires

Les tests fournis couvrent :

- extraction du titre, de l’auteur et du premier chapitre  
- analyse des paragraphes (comptage, arrondi, distribution)  
- cohérence des statistiques générées  

Fichier associé :  
`test_text_processing.py`

Exécution des tests :
`pytest -v`

## Limites actuelles
- Le résumé d’intrigue est volontairement court (respect du copyright)
- Le découpage des chapitres dépend du format exact du texte Gutenberg
- Le graphique est statique (pas d’interactivité)
- Le document Word utilise des styles simples (pas encore de styles avancés personnalisés)
- Le traitement d’image reste basique (recadrage + collage du logo)

---
