import os
import shutil


def create_directories(base_dir):
    """
    Create the necessary directory structure.
    """
    directories = ["reports", "subsidies", "visualizations"]
    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory ensured: {dir_path}")


def move_files(base_dir):
    """
    Move HTML files to their respective folders.
    """
    file_mapping = {
        "PowerBI.html": "reports",
        "enhanced_dashboard.html": "reports",
        "subsidies_heatmap_Code APE_Source Principale.html": "subsidies",
        "subsidies_heatmap_Délai_Alternative 1.html": "subsidies",
        "subsidies_heatmap_Délai_Alternative 2.html": "subsidies",
        "cost_hierarchy.html": "visualizations",
        "flux_financiers_enhanced.html": "visualizations",
        "service_hierarchy.html": "visualizations",
    }

    for file_name, folder in file_mapping.items():
        src = os.path.join(base_dir, file_name)
        dest = os.path.join(base_dir, folder, file_name)

        if os.path.exists(src):
            shutil.move(src, dest)
            print(f"Moved: {src} --> {dest}")
        else:
            print(f"File not found: {src}")


def update_html_paths(base_dir):
    """
    Update paths in HTML files to reflect their new locations.
    """
    html_files = [
        os.path.join(base_dir, "reports", "PowerBI.html"),
        os.path.join(base_dir, "reports", "enhanced_dashboard.html"),
        os.path.join(base_dir, "visualizations", "cost_hierarchy.html"),
        os.path.join(base_dir, "visualizations", "flux_financiers_enhanced.html"),
        os.path.join(base_dir, "visualizations", "service_hierarchy.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Code APE_Source Principale.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Délai_Alternative 1.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Délai_Alternative 2.html"),
    ]

    for html_file_path in html_files:
        if os.path.exists(html_file_path):
            with open(html_file_path, "r", encoding="utf-8") as f:
                content = f.read()

            updated_content = content.replace("html_files/", "")

            with open(html_file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
                print(f"Updated paths in: {html_file_path}")


def create_index_file(base_dir):
    """
    Create an index.html file that redirects to PowerBI.html.
    """
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting to PowerBI Dashboard</title>
    <meta http-equiv="refresh" content="0; url=html_files/reports/PowerBI.html">
</head>
<body>
    <p>If you are not redirected automatically, follow this <a href="html_files/reports/PowerBI.html">link</a>.</p>
</body>
</html>
"""
    index_file_path = os.path.join(base_dir, "index.html")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"Created: {index_file_path}")


def create_readme_file(base_dir):
    """
    Create a README.md file with project details.
    """
    readme_content = """# HTML Dashboard Organization

This repository contains a structured organization of HTML files for visualizations and reports.

## Main File
The main entry point is: `html_files/reports/PowerBI.html`.

## Structure
- `reports/`: Contains analytical dashboards.
- `subsidies/`: Subsidy-related visualizations.
- `visualizations/`: Hierarchies and financial visualizations.

## Usage
1. Open `index.html` in your browser. It will redirect to the main file.
2. Alternatively, navigate directly to `html_files/reports/PowerBI.html`.
"""
    readme_file_path = os.path.join(base_dir, "README.md")
    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Created: {readme_file_path}")


def clean_html_file(file_path):
    """
    Clean up and style an HTML file with proper formatting.
    """
    if os.path.exists(file_path):
        clean_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PowerBI Dashboard</title>
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600&display=swap" rel="stylesheet">
    <!-- Styles -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
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
        .content {
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Welcome to PowerBI Dashboard</h1>
        <p>This is the main entry point for your data visualizations.</p>
    </div>
</body>
</html>
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(clean_content)
        print(f"Cleaned and updated: {file_path}")


def main():
    base_dir = os.path.abspath("html_files")
    print("Starting automation...")

    # Create directories
    create_directories(base_dir)

    # Move files
    move_files(base_dir)

    # Update HTML paths
    update_html_paths(base_dir)

    # Create index.html
    create_index_file(base_dir)

    # Create README.md
    create_readme_file(base_dir)

    # Clean PowerBI.html
    powerbi_path = os.path.join(base_dir, "reports", "PowerBI.html")
    clean_html_file(powerbi_path)

    print("Automation complete!")


if __name__ == "__main__":
    main()
