# templates.py

# Structure HTML de base
HTML_HEAD = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.5">
    <title>EHADS Dashboard</title>
    <link rel="stylesheet" href="/visualisations/assets/css/styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>'''

# Navigation principale
NAVIGATION = '''
<header>
    <nav class="nav-bar">
        <a href="/visualisations/"><img src="/visualisations/assets/logo/ehads_logo.svg" alt="Logo" class="logo"></a>
        <div class="nav-links">
            <a href="/visualisations/html_files/pages/service_architecture.html" class="nav-button active">Service Architecture</a>
            <a href="/visualisations/html_files/pages/cost_analysis.html" class="nav-button">Cost Analysis</a>
            <a href="/visualisations/html_files/pages/subsidies_analysis.html" class="nav-button">Subsidies Analysis</a>
            <a href="/visualisations/html_files/pages/geographic_roadmap.html" class="nav-button">Geographic Roadmap</a>
            <a href="/visualisations/html_files/pages/terms_and_conditions.html" class="nav-button">Conditions Générales</a>
        </div>
    </nav>
</header>'''

# Section service architecture
SERVICE_ARCHITECTURE = '''
<div class="analytics-card">
    <h1>Service Architecture Overview</h1>
    <div class="section">
        <h2>Core Services</h2>
        <ul>
            <li><a href="../visualizations/api_gateway.html">API Gateway Services</a></li>
            <li><a href="../visualizations/microservices.html">Microservices Layout</a></li>
            <li><a href="../visualizations/data_services.html">Data Processing Services</a></li>
            <li><a href="../visualizations/service_hierarchy.html">Service Hierarchy</a></li>
        </ul>
    </div>
    <div class="section">
        <h2>Platform Components</h2>
        <ul>
            <li><a href="../visualizations/security_framework.html">Security Framework</a></li>
            <li><a href="../visualizations/monitoring_system.html">Monitoring System</a></li>
            <li><a href="../visualizations/deployment_pipeline.html">Deployment Pipeline</a></li>
        </ul>
    </div>
</div>'''

# En-tête de la section téléchargement
DOWNLOAD_HEADER = '''
<div class="analytics-card">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.5rem;">
        <div>
            <h2 style="font-size: 1.5rem; font-weight: bold; color: #1a202c;">Téléchargement des Données</h2>
            <p style="color: #4a5568;">Fichiers nettoyés et optimisés pour l'analyse</p>
        </div>
        <i class="fas fa-file-excel" style="color: #3182ce; font-size: 2rem;"></i>
    </div>
    <div class="download-grid">'''

# Template pour chaque élément de téléchargement
DOWNLOAD_ITEM_TEMPLATE = '''
    <div class="download-item">
        <div>
            <p class="file-name">{name}</p>
            <p class="file-message">{message}</p>
        </div>
        <a href="{path}" download class="download-link">
            <i class="fas fa-download"></i>
        </a>
    </div>'''

# Document officiel template
OFFICIAL_DOC_TEMPLATE = '''
<div class="official-doc">
    <h3>Documents Officiels</h3>
    <a href="{pdf_link}" target="_blank" rel="noopener noreferrer" class="doc-link">
        <div>
            <p class="doc-title">{pdf_title}</p>
            <p class="doc-desc">{pdf_desc}</p>
        </div>
        <i class="fas fa-file-pdf"></i>
    </a>
</div>'''

# Template pour le disclaimer
DISCLAIMER_TEMPLATE = '''
<div class="disclaimer-section">
    <h3><i class="fas fa-scale-balanced"></i> {title}</h3>
    <div class="disclaimer-content">
        <p>{text_1}</p>
        <p>{text_2}</p>
        <p class="disclaimer-motto">{motto}</p>
    </div>
</div>'''

# Template pour la section messages
MESSAGES_TEMPLATE = '''
<div class="message-section">
    <p class="message-title">🎯 Message pour MAI Expert</p>
    <p class="message-content">{mai_message}</p>
    
    <p class="message-title">🎩 Message pour Doug's</p>
    <p class="message-content">{doug_message}</p>
</div>'''

# Footer template
FOOTER_TEMPLATE = '''
<footer class="footer">
    <img src="/visualisations/assets/logo/Logo French Tech.png" alt="French Tech" class="footer-logo">
    <p class="footer-text">&copy; 2024 EHADS Dashboard. Tous droits réservés.</p>
</footer>'''

# Styles CSS
STYLES = '''
<style>
    .download-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .download-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem;
        background-color: #f7fafc;
        border-radius: 0.5rem;
        transition: background-color 0.2s;
    }
    .download-item:hover {
        background-color: #ebf8ff;
    }
    .file-name {
        font-weight: 500;
        color: #2d3748;
        margin-bottom: 0.25rem;
    }
    .file-message {
        font-size: 0.875rem;
        color: #718096;
    }
    .download-link {
        color: #3182ce;
        padding: 0.5rem;
    }
    .download-link:hover {
        color: #2c5282;
    }
    .official-doc {
        background: linear-gradient(to right, #ebf8ff, #f3e8ff);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
    }
    .message-section {
        background-color: #ebf8ff;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .message-title {
        font-weight: 500;
        color: #2c5282;
        margin-bottom: 0.5rem;
    }
    .message-content {
        color: #3182ce;
        margin-bottom: 1rem;
    }
    .disclaimer-section {
        background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
        color: white;
        padding: 2rem;
        border-radius: 0.5rem;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .disclaimer-section h3 {
        color: #ffffff;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        text-align: center;
        letter-spacing: 2px;
    }
    .disclaimer-content {
        line-height: 1.6;
    }
    .disclaimer-content p {
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    .disclaimer-motto {
        text-align: center;
        font-style: italic;
        color: #bcd9ff;
        font-size: 1.2rem !important;
        margin-top: 1.5rem;
    }
</style>'''

# Structure de fermeture HTML
HTML_CLOSING = '''
    </body>
</html>'''
