import os

def update_file_paths(directory):
    # Liste tous les fichiers HTML dans le répertoire pages
    files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Met à jour les chemins
        content = content.replace('src="html_viz/', 'src="../visualizations/')
        content = content.replace('href="html_viz/', 'href="../visualizations/')
        content = content.replace('src="subsidies/', 'src="../subsidies/')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated paths in {file}")

# Exécute sur le dossier pages
update_file_paths('html_files/pages')
