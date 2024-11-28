import os
import re
from pathlib import Path

def create_nav_header():
    return '''
    <header>
        <nav class="nav-bar">
            <a href="/"><img src="/logo/ehads_logo.svg" alt="Logo" class="logo" title="Dashboard Analytics"></a>
            <a href="/html_files/pages/service_architecture.html" class="nav-button">Service Architecture</a>
            <a href="/html_files/pages/cost_analysis.html" class="nav-button">Cost Analysis</a>
            <a href="/html_files/pages/subsidies_analysis.html" class="nav-button">Subsidies Analysis</a>
            <a href="/html_files/pages/geographic_roadmap.html" class="nav-button">Geographic Roadmap</a>
            <a href="/html_files/pages/terms_and_conditions.html" class="nav-button">Conditions Générales</a>
        </nav>
    </header>
    '''

def create_footer():
    return '''
    <footer class="footer">
        <div class="footer-content">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
    '''

def create_head_section(title):
    return f'''
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EHADS Dashboard - {title}</title>
        <link rel="stylesheet" href="/css/styles.css">
        <link rel="icon" type="image/svg+xml" href="/logo/ehads_logo.svg">
    </head>
    '''

def get_title_from_content(content):
    # Essaie de trouver un titre dans le contenu HTML
    match = re.search(r'<h1.*?>(.*?)</h1>', content, re.DOTALL) or \
            re.search(r'<title.*?>(.*?)</title>', content, re.DOTALL) or \
            re.search(r'<h2.*?>(.*?)</h2>', content, re.DOTALL)
    return match.group(1).strip() if match else "Dashboard"

def extract_main_content(content):
    # Extrait le contenu principal en supprimant l'ancien header et footer
    content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!DOCTYPE.*?>', '', content, flags=re.DOTALL)
    content = re.sub(r'<html.*?>', '', content, flags=re.DOTALL)
    content = re.sub(r'</html>', '', content, flags=re.DOTALL)
    content = re.sub(r'<head.*?</head>', '', content, flags=re.DOTALL)
    content = re.sub(r'<body.*?>', '', content, flags=re.DOTALL)
    content = re.sub(r'</body>', '', content, flags=re.DOTALL)
    return content.strip()

def update_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire le titre et le contenu principal
        title = get_title_from_content(content)
        main_content = extract_main_content(content)

        # Créer le nouveau contenu HTML
        new_content = f'''<!DOCTYPE html>
<html lang="fr">
{create_head_section(title)}
<body>
    {create_nav_header()}
    <main class="content">
        {main_content}
    </main>
    {create_footer()}
</body>
</html>'''

        # Sauvegarder le fichier mis à jour
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Mise à jour réussie : {file_path}")
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de {file_path}: {str(e)}")

def create_css():
    css_content = """/* Variables globales */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --light-bg: #f8f9fa;
    --dark-bg: #343a40;
}

/* Reset et styles de base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: var(--light-bg);
    padding-top: 60px;
}

/* Navigation */
.nav-bar {
    background-color: var(--dark-bg);
    padding: 1rem;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.nav-button {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.nav-button:hover {
    background-color: var(--primary-color);
}

.logo {
    height: 40px;
    margin-right: 2rem;
}

/* Conteneurs */
.content {
    max-width: 1200px;
    margin: 20px auto;
    padding: 20px;
}

.analytics-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 20px;
    margin-bottom: 20px;
}

/* Footer */
.footer {
    background-color: var(--dark-bg);
    color: white;
    padding: 1rem;
    text-align: center;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Autres styles existants... */
"""
    return css_content

def main():
    # Créer les dossiers nécessaires
    folders = ['css', 'logo', 'html_files/pages']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Créer le fichier CSS
    with open('css/styles.css', 'w', encoding='utf-8') as f:
        f.write(create_css())
    print("✅ Fichier CSS créé")

    # Mettre à jour tous les fichiers HTML
    html_files = Path('.').rglob('*.html')
    for html_file in html_files:
        update_html_file(str(html_file))

if __name__ == "__main__":
    main()
