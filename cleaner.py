import os
from bs4 import BeautifulSoup

def clean_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    if soup.header:
        soup.header.decompose()
    if soup.footer:
        soup.footer.decompose()
    
    main = soup.find('main')
    if main:
        content = main.find('div', class_='analytics-card') or main
    else:
        content = soup.body.find('div', class_='analytics-card')
    
    new_html = BeautifulSoup('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="/visualisations/assets/css/visualization-styles.css">
    </head>
    <body>
        <div class="content"></div>
    </body>
    </html>
    ''', 'html.parser')
    
    if content:
        new_html.find('div', class_='content').append(content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(new_html.prettify()))

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                clean_html_file(file_path)

if __name__ == '__main__':
    directories = [
        'html_files/visualizations',
        'html_files/subsidies'
    ]
    
    for dir_path in directories:
        process_directory(dir_path)
