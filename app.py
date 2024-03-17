from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Route for index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for admin_panel.html
@app.route('/admin_panel')
def admin_panel():
    # Fetch admin_panel.html content from URL
    admin_panel_url = "https://foodorderadmin.onrender.com/admin_panel.html"  # Replace with actual URL
    response = requests.get(admin_panel_url)

    if response.status_code == 200:
        admin_html = response.text

        # Parse admin_panel.html and extract items list
        admin_soup = BeautifulSoup(admin_html, 'html.parser')
        items_list = admin_soup.find_all('div', class_='item')

        # Render admin_panel.html with items list
        return render_template('admin_panel.html', items=items_list)
    else:
        return "Failed to fetch admin_panel.html content. Status code: {}".format(response.status_code)

if __name__ == '__main__':
    app.run(debug=True)
