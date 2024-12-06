#!/usr/bin/env python3
import os
import mimetypes
import sys
import stat
import logging
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DownloadHandler(SimpleHTTPRequestHandler):
   def do_GET(self):
       if self.path.endswith('.csv'):
           self.send_response(200)
           self.send_header('Content-Type', 'text/csv')
           self.send_header('Content-Disposition', 'attachment')
           self.end_headers()
       super().do_GET()

def secure_permissions():
   try:
       csv_dir = Path('./cleaned_final')
       csv_dir.mkdir(exist_ok=True)
       
       # Permissions sécurisées
       os.chmod(csv_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP)
       
       for csv_file in csv_dir.glob('*.csv'):
           os.chmod(csv_file, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)
           
   except Exception as e:
       logger.error(f"Erreur permissions: {e}")

def fix_html():
   try:
       html_path = Path('index.html')
       if not html_path.exists():
           logger.error("index.html non trouvé")
           return

       content = html_path.read_text()

       # Corrections chemins
       replacements = {
           '/visualisations/': './',
           '../cleaned_final/': './cleaned_final/',
           '../visualizations/': './html_files/visualizations/'
       }
       
       for old, new in replacements.items():
           content = content.replace(old, new)

       # Ajout attributs download
       content = content.replace('class="download-link">', 
                               'class="download-link" download>')

       html_path.write_text(content)
       logger.info("HTML corrigé")

   except Exception as e:
       logger.error(f"Erreur HTML: {e}")

def configure_server():
   try:
       # MIME types
       mimetypes.add_type('text/csv', '.csv')
       mimetypes.add_type('text/html', '.html')

       # Server local pour test
       port = 8000
       httpd = HTTPServer(('', port), DownloadHandler)
       logger.info(f"Serveur démarré port {port}")
       return httpd

   except Exception as e:
       logger.error(f"Erreur serveur: {e}")
       return None

def main():
   try:
       logger.info("Début configuration...")
       secure_permissions()
       fix_html()
       
       server = configure_server()
       if server:
           server.serve_forever()
           
   except KeyboardInterrupt:
       logger.info("Arrêt serveur")
       sys.exit(0)
   except Exception as e:
       logger.error(f"Erreur fatale: {e}")
       sys.exit(1)

if __name__ == "__main__":
   main()
