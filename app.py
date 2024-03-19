from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample item data
items_data = {
    '1': {'name': 'Tako', 'quantity': 150, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470283/TG-Foods/Tako_148_qb6ayw.png'},
    '2': {'name': 'Hotdog', 'quantity': 120, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470281/TG-Foods/Hotdog_148_iddyls.png'},
    '3': {'name': 'Burger', 'quantity': 200, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470282/TG-Foods/Burger_148_vm6adu.png'},
    '4': {'name': 'Fries', 'quantity': 250, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470285/TG-Foods/Fries_148_jxcly5.png'},
    '5': {'name': 'Pizza', 'quantity': 300, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470283/TG-Foods/Pizza_148_jej5pz.png'},
    '6': {'name': 'Coke', 'quantity': 50, 'image_url': 'https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470282/TG-Foods/Coke_148_ajethz.png'}
}

@app.route('/')
def index():
    return render_template('index.html', items=items_data)

@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

@app.route('/update-items', methods=['POST'])
def update_items():
    global items_data
    
    data = request.form
    
    # Update items_data based on received data
    items_data = {}
    for key, value in data.items():
        item_id, item_name = key.split('-')
        items_data[item_id] = {'name': item_name, 'quantity': int(value)}
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
