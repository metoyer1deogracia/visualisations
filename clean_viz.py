import os
from pathlib import Path
import re

def clean_visualization_file(file_path):
    """Nettoie les fichiers de visualisation en supprimant les headers/footers redondants"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extrait uniquement le contenu principal (sans header/footer)
        main_content = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)
        if not main_content:
            main_content = re.search(r'<body.*?>(.*?)</body>', content, re.DOTALL)

        if main_content:
            content_only = main_content.group(1)
        else:
            return

        # Nouvelle structure pour les visualisations
        clean_content = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EHADS Visualization</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #1e293b;
            color: #f8fafc;
            font-family: 'Sora', sans-serif;
        }}
        .visualization-container {{
            padding: 20px;
            width: 100%;
            height: 100vh;
            box-sizing: border-box;
        }}
        .metric-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: #1e293b;
        }}
        .trend-up {{
            color: #22c55e;
        }}
        .trend-down {{
            color: #ef4444;
        }}
    </style>
</head>
<body>
    <div class="visualization-container">
        {content_only}
    </div>
</body>
</html>'''

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)

        print(f"✅ Visualization nettoyée : {file_path}")

    except Exception as e:
        print(f"❌ Erreur lors du nettoyage de {file_path}: {str(e)}")

def main():
    print("🧹 Début du nettoyage des visualisations...")
    
    # Chemins des dossiers de visualisation
    viz_paths = [
        './html_files/visualizations',
        './html_files/subsidies'
    ]
    
    for viz_path in viz_paths:
        if os.path.exists(viz_path):
            for file_path in Path(viz_path).rglob('*.html'):
                clean_visualization_file(str(file_path))

    print("✨ Nettoyage des visualisations terminé!")

if __name__ == "__main__":
    main()
