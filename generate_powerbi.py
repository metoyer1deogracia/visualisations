
#!/usr/bin/env python3

def generate_powerbi_dashboard():
    dashboard_content = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Analytics Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
    
    <style>
        :root {
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
            font-family: 'Sora', sans-serif;
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
        
        .analytics-card {
            margin: 20px 0;
            padding: 20px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .metric-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px 0;
        }
        
        .metric-card {
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .metric-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }
        
        .metric-value {
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0.5rem 0;
        }
        
        .metric-trend {
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }

        .visual-content iframe {
            width: 100%;
            height: 600px;
            border: none;
            border-radius: 8px;
        }

        .section {
            margin: 20px 0;
            padding: 20px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 8px;
        }

        .highlight {
            background-color: #e3f2fd;
            padding: 10px;
            border-radius: 4px;
        }

        .opportunity {
            color: #1976d2;
            font-weight: bold;
        }

        .amount {
            color: #2e7d32;
            font-weight: bold;
        }

        .easy { color: #388e3c; }
        .medium { color: #f57c00; }
        .hard { color: #d32f2f; }

        @media (max-width: 768px) {
            .nav-bar {
                flex-direction: column;
                align-items: center;
            }

            .metric-container {
                grid-template-columns: 1fr;
            }

            .visual-content iframe {
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <nav class="nav-bar">
        <button class="nav-button" onclick="showPage('service_hierarchy.html', this)">Service Architecture</button>
        <button class="nav-button" onclick="showPage('cost_analysis.html', this)">Cost Analysis</button>
        <button class="nav-button" onclick="showPage('subsidies_analysis.html', this)">Subsidies Analysis</button>
        <button class="nav-button" onclick="showPage('roadmap.html', this)">Geographic Roadmap</button>
        <button class="nav-button" onclick="showPage('terms_and_conditions', this)">Conditions Générales</button>
    </nav>

    <img>
    alt="Logo" 
         class="logo"
         title="Dashboard Analytics">
'''

    # On écrit la première partie
    with open('PowerBI.html', 'w', encoding='utf-8') as f:
        f.write(dashboard_content)

    print("Première partie du PowerBI.html générée avec succès!")

if __name__ == "__main__":
    generate_powerbi_dashboard()
