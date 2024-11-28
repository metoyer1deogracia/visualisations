import os
from pathlib import Path

def create_css_content():
    return """/* Variables Globales */
:root {
    --primary-dark: #1e293b;
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

/* Base et Typographie */
body {
    font-family: 'Sora', sans-serif;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    background-color: var(--primary-light);
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
    padding: var(--padding-card);
    margin-bottom: 2rem;
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
    background: var(--primary-dark);
    padding: 1.5rem;
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

/* Footer */
.footer {
    background: var(--primary-dark);
    padding: 1.5rem;
    margin-top: 2rem;
}

.logo-container {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 1rem;
}

.footer-text {
    color: white;
    text-align: center;
    font-size: 0.875rem;
}

/* Grids */
.location-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

/* Hub Banner */
.hub-banner {
    background: #dbeafe;
    color: #1e40af;
    padding: 0.5rem;
    border-radius: var(--border-radius);
}

/* Phase Indicator */
.phase {
    border-left: 4px solid #818cf8;
    padding-left: 1rem;
}
"""

def update_css_file():
    css_dir = Path('assets/css')
    css_dir.mkdir(parents=True, exist_ok=True)
    
    css_file = css_dir / 'styles.css'
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(create_css_content())
    print(f"✅ Fichier CSS mis à jour : {css_file}")

def verify_html_files():
    """Vérifie que tous les fichiers HTML ont le bon lien CSS"""
    for html_file in Path('.').rglob('*.html'):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<link rel="stylesheet" href="/visualisations/assets/css/styles.css">' not in content:
            print(f"⚠️ Attention : {html_file} pourrait avoir un mauvais lien CSS")

def main():
    print("🎨 Mise à jour des styles...")
    update_css_file()
    verify_html_files()
    print("\n✨ Styles mis à jour avec succès !")

if __name__ == "__main__":
    main()
