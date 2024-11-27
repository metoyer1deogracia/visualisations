import os

# Directories and files
BASE_DIR = os.getcwd()
HTML_DIR = os.path.join(BASE_DIR, 'html_files')
PAGES_DIR = os.path.join(HTML_DIR, 'pages')
CSS_DIR = os.path.join(HTML_DIR, 'css')
JS_DIR = os.path.join(HTML_DIR, 'js')

# Page names and content
PAGES = {
    "service_architecture.html": "<div class='analytics-card'><h2>Service Architecture</h2><p>Service Hierarchy and Dependencies.</p></div>",
    "cost_analysis.html": "<div class='analytics-card'><h2>Cost Analysis</h2><p>Financial Flux and Cost Hierarchy Analysis.</p></div>",
    "subsidies_analysis.html": "<div class='analytics-card'><h2>Subsidies Analysis</h2><p>Analysis of Available Subsidies and Grants.</p></div>",
    "geographic_roadmap.html": "<div class='analytics-card'><h2>Geographic Roadmap</h2><p>Development Roadmap and Expansion Plans.</p></div>",
    "terms_and_conditions.html": "<div class='analytics-card'><h2>Conditions Générales</h2><p>Conditions légales et fiscales.</p></div>",
}

def create_directories():
    os.makedirs(PAGES_DIR, exist_ok=True)
    os.makedirs(CSS_DIR, exist_ok=True)
    os.makedirs(JS_DIR, exist_ok=True)
    print("Directories created.")

def create_files():
    # Create index.html
    index_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Analytics Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <nav class="nav-bar">
        <button class="nav-button" onclick="loadPage('service_architecture.html', this)">Service Architecture</button>
        <button class="nav-button" onclick="loadPage('cost_analysis.html', this)">Cost Analysis</button>
        <button class="nav-button" onclick="loadPage('subsidies_analysis.html', this)">Subsidies Analysis</button>
        <button class="nav-button" onclick="loadPage('geographic_roadmap.html', this)">Geographic Roadmap</button>
        <button class="nav-button" onclick="loadPage('terms_and_conditions.html', this)">Conditions Générales</button>
    </nav>

    <img src="logo.png" alt="Logo" class="logo" title="Dashboard Analytics">

    <div class="content">
        <div id="page-content">Chargement...</div>
    </div>

    <script src="js/scripts.js"></script>
</body>
</html>"""
    with open(os.path.join(HTML_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Create page files
    for page, content in PAGES.items():
        with open(os.path.join(PAGES_DIR, page), 'w', encoding='utf-8') as f:
            f.write(content)
    print("HTML pages created.")

    # Create CSS and JS files
    with open(os.path.join(CSS_DIR, 'styles.css'), 'w', encoding='utf-8') as f:
        f.write("/* Add your CSS here */")
    with open(os.path.join(JS_DIR, 'scripts.js'), 'w', encoding='utf-8') as f:
        f.write("""/* Add your JS logic here */""")
    print("CSS and JS files created.")

if __name__ == "__main__":
    create_directories()
    create_files()
    print("Setup complete.")
