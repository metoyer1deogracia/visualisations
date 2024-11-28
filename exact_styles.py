import os
from pathlib import Path

def create_exact_styles():
    """Crée le fichier CSS avec les styles exacts des captures d'écran"""
    css_content = """
/* Base */
body {
    font-family: 'Sora', sans-serif;
    background-color: #F5F7FA;
    margin: 0;
    padding-top: 60px;
}

/* Header/Navigation */
.nav-bar {
    background-color: #1e2c3b;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    height: 60px;
    display: flex;
    align-items: center;
    padding: 0 2rem;
}

.nav-button {
    color: #fff;
    text-decoration: none;
    padding: 8px 16px;
    margin: 0 4px;
    border-radius: 4px;
    font-weight: 500;
}

.nav-button.active {
    background-color: #3b82f6;
}

/* Metric Cards */
.metric-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin: 24px 0;
}

.metric-card {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 24px;
}

.metric-header {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 16px;
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 600;
    color: #1e2c3b;
    margin-bottom: 8px;
}

.trend-indicator {
    font-size: 1rem;
    font-weight: 500;
}

.trend-indicator.positive {
    color: #22c55e;
}

.trend-indicator.negative {
    color: #ef4444;
}

/* Content Cards */
.analytics-card {
    background: #FFFFFF;
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 24px;
}

.card-title {
    font-size: 1.875rem;
    font-weight: 600;
    color: #1e2c3b;
    margin-bottom: 8px;
}

.card-subtitle {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 24px;
}

/* Hub Sections */
.hub-section {
    background-color: #EBF3FF;
    padding: 16px;
    border-radius: 4px;
    margin: 16px 0;
}

.hub-title {
    color: #1e40af;
    font-weight: 500;
    margin-bottom: 16px;
}

/* Location Grid */
.location-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
}

.location {
    padding: 24px;
}

.location-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 16px;
}

.location-potential {
    color: #64748b;
    font-size: 0.875rem;
    margin-top: 16px;
}

/* Visualizations */
.viz-container {
    width: 100%;
    height: 800px;
    background-color: #1e2c3b;
    padding: 24px;
    border-radius: 8px;
    margin: 24px 0;
}

/* Footer */
.footer {
    background-color: #1e2c3b;
    padding: 24px;
    text-align: center;
    margin-top: 48px;
}

.footer-logo {
    height: 40px;
    margin-bottom: 16px;
}

.footer-text {
    color: #fff;
    font-size: 0.875rem;
}

/* Utilities */
.phase-indicator {
    border-left: 4px solid #818cf8;
    padding-left: 16px;
    margin: 24px 0;
}
"""
    
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("✅ Styles CSS exacts créés")

def update_html_structure():
    """Met à jour la structure HTML pour correspondre aux captures d'écran"""
    base_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/visualisations/assets/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <nav class="nav-bar">
            <a href="/visualisations/"><img src="/visualisations/assets/logo/ehads_logo.svg" alt="Logo" class="logo"></a>
            <div class="nav-links">
                <a href="/visualisations/html_files/pages/service_architecture.html" class="nav-button">Service Architecture</a>
                <a href="/visualisations/html_files/pages/cost_analysis.html" class="nav-button">Cost Analysis</a>
                <a href="/visualisations/html_files/pages/subsidies_analysis.html" class="nav-button">Subsidies Analysis</a>
                <a href="/visualisations/html_files/pages/geographic_roadmap.html" class="nav-button">Geographic Roadmap</a>
                <a href="/visualisations/html_files/pages/terms_and_conditions.html" class="nav-button">Conditions Générales</a>
            </div>
        </nav>
    </header>
    <main class="content">
        {content}
    </main>
    <footer class="footer">
        <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="footer-logo">
        <p class="footer-text">&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
    </footer>
</body>
</html>"""

    # Trouver et mettre à jour tous les fichiers HTML
    html_files = Path('.').rglob('*.html')
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extraire le contenu principal
            main_content = ""
            if '<main' in content:
                start = content.find('<main')
                end = content.find('</main>') + 7
                main_content = content[start:end]
            
            # Créer le nouveau contenu
            page_title = "EHADS Dashboard"
            if 'title>' in content:
                title_start = content.find('<title>') + 7
                title_end = content.find('</title>')
                page_title = content[title_start:title_end]
            
            new_content = base_html.format(
                title=page_title,
                content=main_content
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"✅ Structure mise à jour : {file_path}")
            
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour de {file_path}: {str(e)}")

def main():
    print("🎨 Début de la mise à jour avec les styles exacts...")
    create_exact_styles()
    update_html_structure()
    print("\n✨ Mise à jour terminée !")

if __name__ == "__main__":
    main()
