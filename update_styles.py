import os
from pathlib import Path

def create_styles():
    """Crée le fichier CSS avec tous les styles standardisés"""
    css_content = """
:root {
    --primary-dark: #dbeafe;
    --primary-light: #f8fafc;
    --accent-blue: #3b82f6;
    --success-green: #22c55e;
    --error-red: #ef4444;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --border-radius: 0.5rem;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
    --padding-card: 1.5rem;
}

/* Base styles */
body {
    font-family: 'Sora', sans-serif;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    background: var(--primary-light);
    margin: 0;
    padding-top: 60px;
}

/* Navigation */
.nav-bar {
    background-color: var(--primary-dark);
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100%;
    box-sizing: border-box;
    z-index: 1000;
}

.nav-button {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: var(--border-radius);
    transition: background-color 0.3s;
}

.nav-button:hover {
    background-color: var(--accent-blue);
}

/* Metric Cards */
.metric-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    margin: 2rem 0;
}

.metric-card {
    background: white;
    border-radius: var(--border-radius);
    padding: var(--padding-card);
    box-shadow: var(--shadow-sm);
}

.metric-value {
    font-size: 2rem;
    font-weight: 600;
    color: var(--text-primary);
}

.trend-indicator {
    font-size: 0.875rem;
}

.trend-indicator.positive {
    color: var(--success-green);
}

.trend-indicator.negative {
    color: var(--error-red);
}

/* Content Cards */
.content-wrapper {
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.analytics-card {
    background: white;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-sm);
    padding: 2rem;
    margin-bottom: 2rem;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

/* Themed Sections */
.themed-section {
    background: #dbeafe;
    border-radius: var(--border-radius);
    padding: 1rem;
    margin: 1rem 0;
}

.section-title {
    color: #1e40af;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

/* Visualizations */
.visualization-container {
    margin: 2rem 0;
    border-radius: var(--border-radius);
    overflow: hidden;
}

.viz-header {
    background: var(--primary-dark);
    color: white;
    padding: 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

/* Lists */
.highlight-list {
    background: #f1f5f9;
    border-radius: var(--border-radius);
    padding: 1.5rem;
    margin: 1rem 0;
}

.key-point {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0;
}

.key-point::before {
    content: "•";
    color: var(--accent-blue);
}

/* Footer */
.footer {
    background: var(--primary-dark);
    padding: 1.5rem;
    color: white;
    margin-top: 3rem;
}

.logo-container {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 1rem;
}

.footer-text {
    text-align: center;
    font-size: 0.875rem;
}

/* Grid Layouts */
.location-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.hub-banner {
    background: #dbeafe;
    color: #1e40af;
    padding: 0.5rem;
    border-radius: 4px;
}
"""
    
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("✅ Styles CSS créés")

def update_html_files():
    """Met à jour tous les fichiers HTML pour utiliser les nouveaux styles"""
    html_files = Path('.').rglob('*.html')
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ajouter les classes appropriées
            content = content.replace('<div class="metric-card">', '<div class="metric-card">')
            content = content.replace('<div class="analytics-card">', '<div class="analytics-card">')
            content = content.replace('<div class="themed-section">', '<div class="themed-section">')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Mis à jour : {file_path}")
        
        except Exception as e:
            print(f"❌ Erreur lors de la mise à jour de {file_path}: {str(e)}")

def main():
    print("🎨 Début de la mise à jour des styles...")
    
    # Créer les styles CSS
    create_styles()
    
    # Mettre à jour les fichiers HTML
    update_html_files()
    
    print("\n✨ Mise à jour des styles terminée !")

if __name__ == "__main__":
    main()
