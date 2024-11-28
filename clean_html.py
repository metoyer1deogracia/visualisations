import os
from pathlib import Path
import re

def clean_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Structure HTML de base
        clean_structure = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EHADS Dashboard</title>
    <link rel="stylesheet" href="/visualisations/assets/css/styles.css">
    <link rel="icon" type="image/svg+xml" href="/visualisations/assets/logo/ehads_logo.svg">
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <nav class="nav-bar">
            <a href="/visualisations/"><img src="/visualisations/assets/logo/ehads_logo.svg" alt="Logo" class="logo" title="Dashboard Analytics"></a>
            <a href="/visualisations/html_files/pages/service_architecture.html" class="nav-button">Service Architecture</a>
            <a href="/visualisations/html_files/pages/cost_analysis.html" class="nav-button">Cost Analysis</a>
            <a href="/visualisations/html_files/pages/subsidies_analysis.html" class="nav-button">Subsidies Analysis</a>
            <a href="/visualisations/html_files/pages/geographic_roadmap.html" class="nav-button">Geographic Roadmap</a>
            <a href="/visualisations/html_files/pages/terms_and_conditions.html" class="nav-button">Conditions Générales</a>
        </nav>
    </header>'''

        # Footer standard
        standard_footer = '''
    <footer class="footer">
        <div class="footer-content">
            <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="french-tech-logo">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
</body>
</html>'''

        # Extraire le contenu principal (tout ce qui est entre header et footer)
        main_content = re.search(r'<main.*?</main>', content, re.DOTALL)
        if main_content:
            main_content = main_content.group(0)
        else:
            main_content = "<main></main>"

        # Supprimer les multiples main
        main_content = re.sub(r'<main.*?<main', '<main', main_content, flags=re.DOTALL)
        main_content = re.sub(r'</main>.*?</main>', '</main>', main_content, flags=re.DOTALL)

        # Assembler le fichier propre
        clean_content = f"{clean_structure}\n{main_content}\n{standard_footer}"

        # Supprimer les liens CSS et logo en double
        clean_content = re.sub(r'/assets/assets/', '/assets/', clean_content)

        # Écrire le fichier nettoyé
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)

        print(f"✅ Nettoyé : {file_path}")
        
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {str(e)}")

def main():
    print("🧹 Début du nettoyage des fichiers HTML...")
    
    # Trouver tous les fichiers HTML dans le projet
    html_files = Path('.').rglob('*.html')
    
    # Nettoyer chaque fichier
    for file_path in html_files:
        clean_html_file(str(file_path))
    
    print("\n✨ Nettoyage terminé !")

if __name__ == "__main__":
    main()
