from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Global variable to store item data
items_data = {}

# Route for index.html
@app.route('/')
def index():
    return render_template('index.html', items=items_data)

# Route for admin-panel.html
@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

# Route to handle adding or removing items
@app.route('/update-items', methods=['POST'])
def update_items():
    global items_data
    
    # Get the data from the POST request
    data = request.form
    
    # Update the items_data dictionary based on the received data
    items_data = {}
    for key, value in data.items():
        item_id, item_name = key.split('-')
        items_data[item_id] = {'name': item_name, 'quantity': int(value)}
    
    # Redirect back to the index route after updating items_data
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
