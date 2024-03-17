from bs4 import BeautifulSoup
import requests

# Read admin_panel.html and extract items list
with open('admin_panel.html', 'r', encoding='utf-8') as admin_file:
    admin_html = admin_file.read()

admin_soup = BeautifulSoup(admin_html, 'html.parser')
items_list = admin_soup.find_all('div', class_='item')

# Update index.html with the items list
with open('index.html', 'r', encoding='utf-8') as index_file:
    index_html = index_file.read()

index_soup = BeautifulSoup(index_html, 'html.parser')
container = index_soup.find('div', class_='inner')

# Clear existing items in container
container.clear()

# Append new items to container
for item in items_list:
    container.append(item)

# Write the updated index.html
with open('index.html', 'w', encoding='utf-8') as updated_index_file:
    updated_index_file.write(str(index_soup))
