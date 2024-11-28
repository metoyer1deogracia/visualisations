import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Crée la structure de répertoires correcte"""
    directories = [
        'html_files/pages',
        'html_files/visualizations',
        'html_files/subsidies',
        'assets/css',
        'assets/js',
        'assets/logo'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def move_files():
    """Déplace les fichiers vers leurs emplacements corrects"""
    # Définition des déplacements de fichiers
    moves = [
        # Déplacer les fichiers CSS
        ('css/styles.css', 'assets/css/styles.css'),
        
        # Déplacer les fichiers JS
        ('js/scripts.js', 'assets/js/scripts.js'),
        
        # Déplacer les logos
        ('logo/ehads_logo.svg', 'assets/logo/ehads_logo.svg'),
        
        # Déplacer les pages principales
        ('pages/cost_analysis.html', 'html_files/pages/cost_analysis.html'),
        ('pages/geographic_roadmap.html', 'html_files/pages/geographic_roadmap.html'),
        ('pages/service_architecture.html', 'html_files/pages/service_architecture.html'),
        ('pages/subsidies_analysis.html', 'html_files/pages/subsidies_analysis.html'),
        ('pages/terms_and_conditions.html', 'html_files/pages/terms_and_conditions.html'),
        
        # Déplacer les visualisations
        ('visualizations/cost_hierarchy.html', 'html_files/visualizations/cost_hierarchy.html'),
        ('visualizations/flux_financiers_enhanced.html', 'html_files/visualizations/flux_financiers_enhanced.html'),
        ('visualizations/service_hierarchy.html', 'html_files/visualizations/service_hierarchy.html'),
        
        # Déplacer les fichiers de subsidies
        ('subsidies/subsidies_heatmap_Code APE_Source Principale.html', 'html_files/subsidies/subsidies_heatmap_Code_APE_Source_Principale.html'),
        ('subsidies/subsidies_heatmap_Délai_Alternative 1.html', 'html_files/subsidies/subsidies_heatmap_Delai_Alternative_1.html'),
        ('subsidies/subsidies_heatmap_Délai_Alternative 2.html', 'html_files/subsidies/subsidies_heatmap_Delai_Alternative_2.html'),
    ]
    
    for src, dst in moves:
        try:
            if os.path.exists(src):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(src, dst)
                print(f"✅ Déplacé : {src} -> {dst}")
        except Exception as e:
            print(f"❌ Erreur lors du déplacement de {src}: {str(e)}")

def clean_old_directories():
    """Supprime les anciens répertoires vides"""
    dirs_to_remove = ['css', 'js', 'logo', 'pages', 'subsidies', 'visualizations']
    for dir_name in dirs_to_remove:
        try:
            if os.path.exists(dir_name) and not os.listdir(dir_name):
                os.rmdir(dir_name)
                print(f"✅ Supprimé répertoire vide : {dir_name}")
        except Exception as e:
            print(f"❌ Erreur lors de la suppression de {dir_name}: {str(e)}")

def update_html_paths():
    """Met à jour les chemins dans tous les fichiers HTML"""
    for html_file in Path('.').rglob('*.html'):
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Mise à jour des chemins
            content = content.replace('"/css/', '"/assets/css/')
            content = content.replace('"/js/', '"/assets/js/')
            content = content.replace('"/logo/', '"/assets/logo/')
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Mis à jour les chemins dans : {html_file}")
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour de {html_file}: {str(e)}")

def main():
    print("🚀 Début de la réorganisation du projet...")
    
    create_directory_structure()
    print("✅ Structure de répertoires créée")
    
    move_files()
    print("✅ Fichiers déplacés")
    
    clean_old_directories()
    print("✅ Anciens répertoires nettoyés")
    
    update_html_paths()
    print("✅ Chemins mis à jour dans les fichiers HTML")
    
    print("\n✨ Réorganisation terminée !")

if __name__ == "__main__":
    main()
