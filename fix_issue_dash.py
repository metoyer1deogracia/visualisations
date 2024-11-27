#!/usr/bin/env python3

def fix_dashboard_script():
    """Create and fix the dashboard generator script."""
    
    # Write the corrected content to dashboard_generator.py
    with open('dashboard_generator.py', 'w', encoding='utf-8') as f:
        f.write('''#!/usr/bin/env python3

import os
from datetime import datetime

class DashboardGenerator:
    def __init__(self):
        """Initialize the dashboard generator with necessary directories."""
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_viz_dir = os.path.join(self.base_dir, 'html_viz')
        self.ensure_directories()

    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        directories = ['html_viz', 'static']
        for directory in directories:
            dir_path = os.path.join(self.base_dir, directory)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"Created directory: {directory}")

    def generate_html_file(self):
        """Generate the main PowerBI.html file."""
        html_content = self.get_html_template()
        
        with open('PowerBI.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("Generated PowerBI.html successfully")

    def create_visualization_files(self):
        """Create visualization HTML files in the html_viz directory."""
        visualizations = [
            'service_hierarchy.html',
            'cost_hierarchy.html',
            'flux_financiers_enhanced.html',
            'subsidies_heatmap_Code APE_Source Principale.html',
            'subsidies_heatmap_Délai_Alternative 1.html',
            'subsidies_heatmap_Délai_Alternative 2.html',
            'funding_treemap.html'
        ]

        for viz in visualizations:
            viz_path = os.path.join(self.html_viz_dir, viz)
            if not os.path.exists(viz_path):
                with open(viz_path, 'w', encoding='utf-8') as f:
                    f.write(f"""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>{viz}</title>
                        <meta charset="UTF-8">
                    </head>
                    <body>
                        <div id="visualization">
                            <!-- Placeholder for {viz} visualization -->
                        </div>
                    </body>
                    </html>
                    """)
                print(f"Created visualization file: {viz}")

    def update_all(self):
        """Update all dashboard files."""
        try:
            self.ensure_directories()
            self.generate_html_file()
            self.create_visualization_files()
            print("Dashboard files updated successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise

def main():
    try:
        generator = DashboardGenerator()
        generator.update_all()
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
''')

    print("Created fixed dashboard generator script")

# Execute the fix
if __name__ == "__main__":
    try:
        fix_dashboard_script()
        print("\nYou can now run the dashboard generator using:")
        print("python3 dashboard_generator.py")
    except Exception as e:
        print(f"Error while fixing the script: {str(e)}")
