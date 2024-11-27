import os

# Base directories
BASE_DIR = os.getcwd()
HTML_DIR = os.path.join(BASE_DIR, 'html_files')
CSS_DIR = os.path.join(HTML_DIR, 'css')
JS_DIR = os.path.join(HTML_DIR, 'js')

# Create directories
def create_directories():
    os.makedirs(CSS_DIR, exist_ok=True)
    os.makedirs(JS_DIR, exist_ok=True)
    print(f"Directories created: {CSS_DIR}, {JS_DIR}")

# Create index.html
def create_index_html():
    content = """<!DOCTYPE html>
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
        <button class="nav-button" onclick="showPage('service_hierarchy', this)">Service Architecture</button>
        <button class="nav-button" onclick="showPage('cost_analysis', this)">Cost Analysis</button>
        <button class="nav-button" onclick="showPage('subsidies_analysis', this)">Subsidies Analysis</button>
        <button class="nav-button" onclick="showPage('roadmap', this)">Geographic Roadmap</button>
        <button class="nav-button" onclick="showPage('terms_and_conditions', this)">Conditions Générales</button>
    </nav>

    <img src="logo.png" alt="Logo" class="logo" title="Dashboard Analytics">

    <div class="content">
        <!-- Service Hierarchy Page -->
        <div class="page-container" id="service_hierarchy">
            <!-- Content for Service Hierarchy -->
        </div>

        <!-- Cost Analysis Page -->
        <div class="page-container" id="cost_analysis">
            <!-- Content for Cost Analysis -->
        </div>

        <!-- Subsidies Analysis Page -->
        <div class="page-container" id="subsidies_analysis">
            <!-- Content for Subsidies Analysis -->
        </div>

        <!-- Geographic Roadmap Page -->
        <div class="page-container" id="roadmap">
            <!-- Content for Geographic Roadmap -->
        </div>

        <!-- Terms and Conditions Page -->
        <div class="page-container" id="terms_and_conditions">
            <!-- Content for Terms and Conditions -->
        </div>
    </div>

    <script src="js/scripts.js"></script>
</body>
</html>
"""
    with open(os.path.join(HTML_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html created.")

# Create styles.css
def create_styles_css():
    content = """:root {
    --primary-color: #2C3E50;
    --secondary-color: #3498DB;
    --accent-color: #4EC9B0;
    --background-color: #B3CEE2;
    --text-color: #1E2A38;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Sora', sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
}

.nav-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(44, 62, 80, 0.95);
    padding: 15px;
    display: flex;
    justify-content: center;
    gap: 20px;
    z-index: 900;
    backdrop-filter: blur(10px);
}

.logo {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 80px;
    height: 80px;
    z-index: 1000;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.8; }
    100% { transform: scale(1); opacity: 1; }
}

.nav-button {
    padding: 12px 24px;
    background: var(--primary-color);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.nav-button:hover {
    background: var(--secondary-color);
    transform: translateY(-2px);
}

.nav-button.active {
    background: var(--secondary-color);
}

.content {
    margin-top: 80px;
    padding: 20px;
}

.page-container {
    display: none;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.page-container.active {
    display: block;
    opacity: 1;
}
"""
    with open(os.path.join(CSS_DIR, 'styles.css'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("styles.css created.")

# Create scripts.js
def create_scripts_js():
    content = """function showPage(pageId, btn) {
    document.querySelectorAll('.page-container').forEach(page => {
        page.classList.remove('active');
    });

    document.querySelectorAll('.nav-button').forEach(button => {
        button.classList.remove('active');
    });

    document.getElementById(pageId).classList.add('active');
    btn.classList.add('active');
    trackPageView(btn.textContent);
}

document.addEventListener('DOMContentLoaded', function() {
    const firstButton = document.querySelector('.nav-button');
    const firstPage = document.querySelector('.page-container');
    if (firstButton && firstPage) {
        firstButton.classList.add('active');
        firstPage.classList.add('active');
    }
});

function trackPageView(pageName) {
    console.log(`Page viewed: ${pageName}`);
    // Integrate your analytics tracking here.
}
"""
    with open(os.path.join(JS_DIR, 'scripts.js'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("scripts.js created.")

# Main function
if __name__ == "__main__":
    print("Setting up modularized dashboard...")
    create_directories()
    create_index_html()
    create_styles_css()
    create_scripts_js()
    print("Modularized dashboard setup complete.")
