# generator.py
import os
from config import FILES_CONFIG, SPECIAL_SECTIONS, EXTERNAL_LINKS
from templates import (
    HTML_HEAD, NAVIGATION, SERVICE_ARCHITECTURE, DOWNLOAD_HEADER,
    DOWNLOAD_ITEM_TEMPLATE, OFFICIAL_DOC_TEMPLATE, DISCLAIMER_TEMPLATE,
    MESSAGES_TEMPLATE, FOOTER_TEMPLATE, STYLES, HTML_CLOSING
)

def generate_download_items():
    """Génère la section de téléchargement pour tous les fichiers configurés."""
    return ''.join([
        DOWNLOAD_ITEM_TEMPLATE.format(
            name=file['name'],
            message=file['message'],
            path=file['path']
        ) for file in FILES_CONFIG
    ])

def generate_official_doc():
    """Génère la section document officiel avec le PDF."""
    return OFFICIAL_DOC_TEMPLATE.format(
        pdf_link=EXTERNAL_LINKS['pdf_report'],
        pdf_title=EXTERNAL_LINKS['pdf_title'],
        pdf_desc=EXTERNAL_LINKS['pdf_desc']
    )

def generate_disclaimer():
    """Génère la section disclaimer avec la devise LEX | LIBERTAS | CIVIS."""
    return DISCLAIMER_TEMPLATE.format(
        title=SPECIAL_SECTIONS['disclaimer_title'],
        text_1=SPECIAL_SECTIONS['disclaimer_text'],
        text_2=SPECIAL_SECTIONS['disclaimer_text_2'],
        motto=SPECIAL_SECTIONS['disclaimer_motto']
    )

def generate_messages():
    """Génère la section des messages pour MAI Expert et Doug's."""
    return MESSAGES_TEMPLATE.format(
        mai_message=SPECIAL_SECTIONS['mai_expert_message'],
        doug_message=SPECIAL_SECTIONS['doug_message']
    )

def generate_html():
    """Génère le fichier HTML complet en assemblant toutes les sections."""
    try:
        with open('index.html', 'w', encoding='utf-8') as f:
            # Structure de base
            f.write(HTML_HEAD)
            f.write('<body>')
            
            # Navigation
            f.write(NAVIGATION)
            
            # Contenu principal
            f.write('<main class="content">')
            
            # Service Architecture
            f.write(SERVICE_ARCHITECTURE)
            
            # Section téléchargements
            f.write(DOWNLOAD_HEADER)
            f.write(generate_download_items())
            f.write('</div>')  # Fermeture de download-grid
            
            # Documents officiels
            f.write(generate_official_doc())
            
            # Disclaimer
            f.write(generate_disclaimer())
            
            # Messages
            f.write(generate_messages())
            
            # Fermeture de la carte analytique et du main
            f.write('</div></main>')
            
            # Footer
            f.write(FOOTER_TEMPLATE)
            
            # Styles
            f.write(STYLES)
            
            # Fermeture HTML
            f.write(HTML_CLOSING)
            
        print("Le fichier index.html a été généré avec succès.")
        return True
        
    except Exception as e:
        print(f"Erreur lors de la génération du fichier : {str(e)}")
        return False

if __name__ == "__main__":
    generate_html()
