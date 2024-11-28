import os
import re
from pathlib import Path

def fix_css_links(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si le head existe
        head_pattern = re.compile(r'<head>.*?</head>', re.DOTALL)
        if not head_pattern.search(content):
            # Ajouter un head complet si manquant
            new_head = '''<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EHADS Visualization</title>
    <link rel="stylesheet" href="/visualisations/assets/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>'''
            content = content.replace('<!DOCTYPE html>\n<html lang="fr">', 
                                   f'<!DOCTYPE html>\n<html lang="fr">\n{new_head}')
        else:
            # Ajouter ou mettre à jour le lien CSS dans le head existant
            css_link = '<link rel="stylesheet" href="/visualisations/assets/css/styles.css">'
            if css_link not in content:
                content = content.replace('</head>', f'    {css_link}\n</head>')

        # Écrire le contenu mis à jour
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Liens CSS corrigés dans : {file_path}")
        
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de {file_path}: {str(e)}")

def main():
    print("🔍 Recherche des fichiers HTML à corriger...")
    
    # Liste des dossiers à vérifier
    directories = [
        'html_files/subsidies',
        'html_files/visualizations',
        'html_files/pages',
        '.'  # Dossier racine
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            for file_path in Path(directory).glob('*.html'):
                fix_css_links(str(file_path))
    
    print("\n✨ Correction des liens CSS terminée !")

if __name__ == "__main__":
    main()
