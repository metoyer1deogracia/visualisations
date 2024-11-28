import os

def fix_paths(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                
                content = content.replace('="/assets/', '="/visualisations/assets/')
                content = content.replace('="/html_files/', '="/visualisations/html_files/')
                
                with open(filepath, 'w') as f:
                    f.write(content)

fix_paths('.')
