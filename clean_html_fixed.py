import os
import re
from pathlib import Path

def read_file_safely(file_path):
    """Lit le fichier en gérant les caractères spéciaux"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def write_file_safely(file_path, content):
    """Écrit le fichier en gérant les caractères spéciaux"""
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(content)

def extract_main_content(content):
    """Extrait le contenu principal en gérant les cas problématiques"""
    try:
        # Chercher le contenu entre les balises main
        main_match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL | re.IGNORECASE)
        if main_match:
            main_content = main_match.group(1)
            return f'<main class="content">{main_content}</main>'
        return '<main class="content"></main>'
    except Exception as e:
        print(f"⚠️ Attention lors de l'extraction du contenu: {str(e)}")
        return '<main class="content"></main>'

def create_clean_structure(main_content, title="EHADS Dashboard"):
    """Crée une structure HTML propre"""
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
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
    </header>
    {main_content}
    <footer class="footer">
        <div class="footer-content">
            <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="french-tech-logo">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
</body>
</html>'''

def clean_file(file_path):
    """Nettoie un fichier HTML"""
    try:
        # Lire le contenu
        content = read_file_safely(file_path)
        
        # Extraire le titre si présent
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        title = title_match.group(1) if title_match else "EHADS Dashboard"
        
        # Extraire le contenu principal
        main_content = extract_main_content(content)
        
        # Créer le nouveau contenu
        new_content = create_clean_structure(main_content, title)
        
        # Écrire le fichier
        write_file_safely(file_path, new_content)
        print(f"✅ Nettoyé : {file_path}")
        
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {str(e)}")

def main():
    print("🧹 Début du nettoyage des fichiers HTML...")
    
    # Nettoyer tous les fichiers HTML
    for file_path in Path('.').rglob('*.html'):
        clean_file(str(file_path))
    
    print("\n✨ Nettoyage terminé !")

if __name__ == "__main__":
    main()
