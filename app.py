from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://noureddine:yeZ1JYO0d9SqDdMyVL2BW14xSivEXm1G@dpg-cnsu8p5a73kc73b713u0-a:5432/itemsdb'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Create tables based on the defined models
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Fetch items from the database
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/admin-panel')
def admin_panel():
    items = Item.query.all()
    return render_template('admin-panel.html', items=items)

# Route to add item to the database
@app.route('/add-item', methods=['POST'])
def add_item():
    data = request.get_json()
    try:
        new_item = Item(title=data['title'], price=data['price'], image_url=data['image_url'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Route to update item price in the database
@app.route('/update-item-price', methods=['POST'])
def update_item_price():
    data = request.get_json()
    try:
        item = Item.query.get(data['id'])
        if item:
            item.price = data['price']
            db.session.commit()
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Route to remove item from the database
@app.route('/remove-item', methods=['POST'])
def remove_item():
    data = request.get_json()
    try:
        item = Item.query.get(data['id'])
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
