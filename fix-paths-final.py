import os
from pathlib import Path

def update_file_paths():
    # Déplacer funding_treemap.html
    if os.path.exists('funding_treemap.html'):
        os.rename('funding_treemap.html', 'html_files/visualizations/funding_treemap.html')
        print("✅ Déplacé funding_treemap.html")

    # Mise à jour des chemins dans tous les fichiers HTML
    for html_file in Path('.').rglob('*.html'):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Correction des chemins pour GitHub Pages
        content = content.replace('href="/', 'href="/visualisations/')
        content = content.replace('src="/', 'src="/visualisations/')
        content = content.replace('/css/', '/assets/css/')
        content = content.replace('/js/', '/assets/js/')
        content = content.replace('/logo/', '/assets/logo/')

        # S'assurer que les liens de navigation sont corrects
        nav_links = '''
        <nav class="nav-bar">
            <a href="/visualisations/"><img src="/visualisations/assets/logo/ehads_logo.svg" alt="Logo" class="logo" title="Dashboard Analytics"></a>
            <a href="/visualisations/html_files/pages/service_architecture.html" class="nav-button">Service Architecture</a>
            <a href="/visualisations/html_files/pages/cost_analysis.html" class="nav-button">Cost Analysis</a>
            <a href="/visualisations/html_files/pages/subsidies_analysis.html" class="nav-button">Subsidies Analysis</a>
            <a href="/visualisations/html_files/pages/geographic_roadmap.html" class="nav-button">Geographic Roadmap</a>
            <a href="/visualisations/html_files/pages/terms_and_conditions.html" class="nav-button">Conditions Générales</a>
        </nav>
        '''
        
        # Remplacer la navigation existante
        content = content.replace('<nav class="nav-bar">', nav_links)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Mis à jour : {html_file}")

if __name__ == "__main__":
    update_file_paths()
    print("\n✨ Mise à jour terminée !")
