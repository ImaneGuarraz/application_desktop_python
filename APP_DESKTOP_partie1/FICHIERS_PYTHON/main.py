# main.py

"""
Interface graphique Tkinter pour l'application d'analyse de données.
Version modernisée : un seul bouton "Analyser le document".
"""

import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"   # supprime un warning Tkinter sur macOS

import tkinter as tk   # interface graphique
from tkinter import filedialog, messagebox   # boîtes de dialogue

from database import (
    create_table,
    clear_database,
    get_all_items,
    is_database_empty,
    aggregate_sum,
    aggregate_avg,
)

from service import import_from_file, import_from_url   # importation universelle
from charts import show_chart_in_window   # affichage du graphique
import config   # thème et configuration visuelle


create_table()   # crée la table SQLite au lancement


def main():
    root = tk.Tk()   # fenêtre principale
    root.title("Analyse de données")
    root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")   # taille fenêtre
    root.configure(bg=config.BG_COLOR)   # couleur de fond

    sidebar = tk.Frame(root, width=250, bg=config.SIDEBAR_COLOR)   # menu latéral
    sidebar.pack(side="left", fill="y")

    content = tk.Frame(root, bg=config.BG_COLOR)   # zone centrale dynamique
    content.pack(side="right", fill="both", expand=True)

    tk.Label(
        content,
        text="Importez un document puis analysez-le",
        bg=config.BG_COLOR,
        fg=config.TEXT_COLOR,
        font=config.LABEL_FONT
    ).pack(pady=40)

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()   # supprime tous les widgets affichés

    def create_card(parent):
        card = tk.Frame(
            parent,
            bg=config.CARD_BG,
            bd=1,
            relief="solid",
            highlightthickness=0
        )   # card iOS (fond clair + bordure légère)
        card.pack(pady=15, padx=40, fill="x")   # marges autour de la card
        return card

    def action_import_file():
        filepath = filedialog.askopenfilename(   # ouvre un sélecteur de fichier
            title="Choisir un fichier",
            filetypes=[
                ("Tous les fichiers", "*.*"),
                ("Texte / CSV", "*.txt *.csv"),
                ("JSON", "*.json"),
                ("Word", "*.docx"),
                ("Excel", "*.xlsx"),
            ]
        )
        if not filepath:
            return

        import_from_file(filepath)   # import universel du fichier
        clear_content()
        card = create_card(content)   # card de confirmation
        tk.Label(
            card,
            text="Fichier importé avec succès",
            bg=config.CARD_BG,
            fg=config.ACCENT_COLOR,
            font=config.LABEL_FONT
        ).pack(pady=20)

    def action_import_url():
        def do_import():
            url = url_entry.get().strip()   # récupère l'URL saisie
            if not url:
                messagebox.showerror("Erreur", "Veuillez entrer une URL")
                return

            try:
                import_from_url(url)   # import universel depuis URL
                popup.destroy()
                clear_content()
                card = create_card(content)   # card de confirmation
                tk.Label(
                    card,
                    text="Données importées depuis l'URL",
                    bg=config.CARD_BG,
                    fg=config.ACCENT_COLOR,
                    font=config.LABEL_FONT
                ).pack(pady=20)
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

        popup = tk.Toplevel(root)   # fenêtre popup pour saisir l'URL
        popup.title("Importer depuis une URL")
        popup.configure(bg=config.BG_COLOR)

        tk.Label(popup, text="URL :", bg=config.BG_COLOR, fg=config.TEXT_COLOR).pack(pady=5)
        url_entry = tk.Entry(popup, width=50)   # champ texte URL
        url_entry.pack(pady=5)

        tk.Button(popup, text="Importer", command=do_import).pack(pady=10)

    def action_analyze():
        clear_content()
        rows = get_all_items()   # récupère toutes les données stockées

        if not rows:
            card = create_card(content)
            tk.Label(
                card,
                text="Aucune donnée à analyser",
                bg=config.CARD_BG,
                fg=config.TEXT_COLOR,
                font=config.LABEL_FONT
            ).pack(pady=20)
            return

        total = aggregate_sum()   # calcule la somme
        avg = aggregate_avg()     # calcule la moyenne

        card_stats = create_card(content)   # card pour les agrégations
        tk.Label(
            card_stats,
            text="Agrégations",
            bg=config.CARD_BG,
            fg=config.TEXT_COLOR,
            font=config.TITLE_FONT
        ).pack(pady=(15, 5))

        tk.Label(
            card_stats,
            text=f"Somme : {total}",
            bg=config.CARD_BG,
            fg=config.ACCENT_COLOR,
            font=("SF Pro Display", 18, "bold")
        ).pack(pady=5)

        tk.Label(
            card_stats,
            text=f"Moyenne : {avg:.3f}",
            bg=config.CARD_BG,
            fg=config.ACCENT_COLOR,
            font=("SF Pro Display", 18, "bold")
        ).pack(pady=5)

        card_chart = create_card(content)   # card pour le graphique
        tk.Label(
            card_chart,
            text="Graphiques",
            bg=config.CARD_BG,
            fg=config.TEXT_COLOR,
            font=config.TITLE_FONT
        ).pack(pady=(15, 5))

        show_chart_in_window(card_chart, rows)   # affiche le graphique dans la card

    def add_menu_button(text, cmd):
        btn = tk.Button(
            sidebar,
            text=text,
            command=cmd,
            bg=config.BTN_COLOR,
            fg=config.TEXT_COLOR,
            activebackground=config.BTN_HOVER,
            activeforeground=config.TEXT_COLOR,
            relief="flat",
            font=config.BTN_FONT,
            height=2
        )   # bouton iOS-like
        btn.pack(fill="x", pady=8, padx=15)

    tk.Label(
        sidebar,
        text="Menu",
        bg=config.SIDEBAR_COLOR,
        fg=config.TEXT_COLOR,
        font=config.TITLE_FONT
    ).pack(pady=20)

    add_menu_button("Importer un document", action_import_file)   # bouton import fichier
    add_menu_button("Importer depuis une URL", action_import_url)   # bouton import URL
    add_menu_button("Analyser le document", action_analyze)   # bouton analyse
    add_menu_button("Effacer la base", clear_database)   # bouton reset DB

    root.mainloop()   # boucle Tkinter


if __name__ == "__main__":
    main()   # lance l'application
