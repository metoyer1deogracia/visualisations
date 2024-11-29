import os

def update_head_section(content):
    """Modifie la section head en ajoutant les favicons."""
    favicon_links = '''    <link rel="icon" type="image/svg+xml" href="/visualisations/assets/logo/ehads_logo.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="/visualisations/assets/logo/ehads_logo.svg">
    <link rel="shortcut icon" type="image/svg+xml" href="/visualisations/assets/logo/ehads_logo.svg">
</head>'''
    
    return content.replace('</head>', favicon_links)

def process_file(file_path):
    """Traite un fichier HTML individuel."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Mise à jour du contenu
        updated_content = update_head_section(content)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Mise à jour réussie : {file_path}")
        return True
    except Exception as e:
        print(f"Erreur lors de la mise à jour de {file_path}: {str(e)}")
        return False

def update_all_pages():
    """Met à jour index.html et tous les fichiers HTML dans le dossier pages."""
    # Liste des fichiers à mettre à jour
    files_to_update = ['index.html']
    
    # Ajout des fichiers du dossier pages
    pages_dir = 'html_files/pages'
    for file in os.listdir(pages_dir):
        if file.endswith('.html'):
            files_to_update.append(os.path.join(pages_dir, file))
    
    # Traitement de chaque fichier
    success_count = 0
    for file_path in files_to_update:
        if process_file(file_path):
            success_count += 1
    
    print(f"\nRésumé des opérations:")
    print(f"- Total des fichiers traités: {len(files_to_update)}")
    print(f"- Mises à jour réussies: {success_count}")
    print(f"- Échecs: {len(files_to_update) - success_count}")

if __name__ == "__main__":
    update_all_pages()
