import os
from pathlib import Path
import re

def update_footer_in_file(file_path):
    # Nouveau footer avec le logo French Tech
    new_footer = '''    <footer class="footer">
        <div class="footer-content">
            <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="french-tech-logo">
            <p>&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
        </div>
    </footer>
</body>
</html>'''

    try:
        # Lire le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remplacer le footer existant
        # Cette regex cherche tout le contenu entre <footer> et </html>
        updated_content = re.sub(
            r'<footer.*?</html>',
            new_footer,
            content,
            flags=re.DOTALL
        )

        # Écrire le contenu mis à jour
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✅ Footer mis à jour dans : {file_path}")
        
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de {file_path}: {str(e)}")

def main():
    # Trouver tous les fichiers HTML dans le projet
    html_files = Path('.').rglob('*.html')
    
    print("🔍 Recherche des fichiers HTML...")
    
    # Mettre à jour chaque fichier
    for file_path in html_files:
        update_footer_in_file(str(file_path))
    
    print("\n✨ Mise à jour des footers terminée !")

if __name__ == "__main__":
    main()
