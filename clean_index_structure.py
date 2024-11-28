import os
import re

def clean_index_first():
    """Nettoie d'abord l'index.html pour en faire une référence"""
    clean_content = '''<!DOCTYPE html>
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
    </header>
    <main class="content">
        <div class="analytics-card">
            <h1>EHADS Dashboard Overview</h1>
            
            <div class="section">
                <h2>Visualisations Principales</h2>
                <ul>
                    <li><a href="/visualisations/html_files/visualizations/cost_hierarchy.html">Hiérarchie des Coûts</a></li>
                    <li><a href="/visualisations/html_files/visualizations/flux_financiers_enhanced.html">Flux Financiers</a></li>
                    <li><a href="/visualisations/html_files/visualizations/funding_treemap.html">Carte des Financements</a></li>
                    <li><a href="/visualisations/html_files/visualizations/service_hierarchy.html">Hiérarchie des Services</a></li>
                </ul>
            </div>

            <div class="section">
                <h2>Analyses des Subventions</h2>
                <ul>
                    <li><a href="/visualisations/html_files/subsidies/subsidies_heatmap_Code_APE_Source_Principale.html">Analyse par Code APE</a></li>
                    <li><a href="/visualisations/html_files/subsidies/subsidies_heatmap_Delai_Alternative_1.html">Analyse des Délais - Version 1</a></li>
                    <li><a href="/visualisations/html_files/subsidies/subsidies_heatmap_Delai_Alternative_2.html">Analyse des Délais - Version 2</a></li>
                </ul>
            </div>
        </div>
    </main>
    <footer class="footer">
        <div class="footer-content">
            <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="french-tech-logo">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
</body>
</html>'''

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(clean_content)
    print("✅ Index.html nettoyé et standardisé")

def clean_other_files(file_path):
    """Nettoie les autres fichiers HTML en utilisant la même structure"""
    if file_path == 'index.html':
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire le contenu principal uniquement (entre <main> et </main>)
        main_content = re.search(r'<main.*?</main>', content, re.DOTALL)
        if main_content:
            main_content = main_content.group(0)
            # Nettoyer les balises main multiples si présentes
            main_content = re.sub(r'<main.*?<main', '<main', main_content, flags=re.DOTALL)
            main_content = re.sub(r'</main>.*?</main>', '</main>', main_content, flags=re.DOTALL)
        else:
            main_content = "<main class='content'></main>"

        # Utiliser la même structure que index.html
        with open('index.html', 'r', encoding='utf-8') as f:
            template = f.read()

        # Remplacer le main du template par le main du fichier actuel
        new_content = re.sub(
            r'<main.*?</main>',
            main_content,
            template,
            flags=re.DOTALL
        )

        # Écrire le fichier nettoyé
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Nettoyé : {file_path}")
    
    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {str(e)}")

def main():
    print("🧹 Début du nettoyage des fichiers HTML...")
    
    # D'abord nettoyer index.html
    clean_index_first()
    
    # Puis nettoyer tous les autres fichiers HTML
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                clean_other_files(file_path)
    
    print("\n✨ Nettoyage terminé !")

if __name__ == "__main__":
    main()
