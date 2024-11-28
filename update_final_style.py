import os
from pathlib import Path

def update_html_files():
    # Le nouveau footer avec le logo French Tech
    new_footer = '''
    <footer class="footer">
        <div class="footer-content">
            <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="french-tech-logo">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
    '''

    # La nouvelle navigation
    new_nav = '''
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
    '''

    # Nouveau head avec Sora font
    new_head = '''
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EHADS Dashboard</title>
        <link rel="stylesheet" href="/visualisations/assets/css/styles.css">
        <link rel="icon" type="image/svg+xml" href="/visualisations/assets/logo/ehads_logo.svg">
        <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    </head>
    '''

    # Mise à jour de tous les fichiers HTML
    for html_file in Path('.').rglob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remplacer le head, nav et footer
            content = content.replace('<head>', new_head)
            content = content.replace('<nav class="nav-bar">', new_nav)
            content = content.replace('<footer class="footer">', new_footer)

            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Mis à jour : {html_file}")
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour de {html_file}: {str(e)}")

def update_css():
    # Nouveau contenu CSS avec vos préférences
    css_content = '''
    :root {
        --primary-bg: #1e293b;
        --secondary-bg: #f8fafc;
        --accent-blue: #3b82f6;
        --text-light: #f1f5f9;
        --text-dark: #0f172a;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Sora', sans-serif;
    }

    body {
        background-color: var(--secondary-bg);
        line-height: 1.6;
        padding-top: 60px;
    }

    .nav-bar {
        background-color: var(--primary-bg);
        padding: 1rem 2rem;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
        display: flex;
        align-items: center;
        gap: 2rem;
    }

    .logo {
        height: 50px;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .french-tech-logo {
        height: 40px;
        margin-bottom: 1rem;
    }

    .nav-button {
        color: var(--text-light);
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        transition: background-color 0.3s;
    }

    .nav-button:hover {
        background-color: var(--accent-blue);
    }

    .footer {
        background-color: var(--primary-bg);
        color: var(--text-light);
        padding: 2rem;
        position: fixed;
        bottom: 0;
        width: 100%;
    }

    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }

    .content {
        max-width: 1200px;
        margin: 80px auto 100px;
        padding: 20px;
    }

    .analytics-card {
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    '''

    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("✅ CSS mis à jour")

if __name__ == "__main__":
    update_css()
    update_html_files()
    print("\n✨ Mise à jour terminée !")
