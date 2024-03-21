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

# @app.route('/admin-panel')
# def admin_panel():
#     return render_template('admin-panel.html')

@app.route('/admin-panel')
def admin_panel():
    # Fetch items from the database
    items = Item.query.all()
    return render_template('admin-panel.html', items=items)

@app.route('/update-items', methods=['POST'])
def update_items():
    try:
        # Get the JSON data sent from the client-side
        data = request.get_json()
        
        # Iterate over each item in the received data
        with app.app_context():
            for item_data in data:
                # Check if the item with the same name already exists in the database
                existing_item = Item.query.filter_by(title=item_data['title']).first()
                if existing_item:
                    # If the item exists, update its price and image URL
                    existing_item.price = item_data['price']
                    existing_item.image_url = item_data['image']
                else:
                    # If the item does not exist, create a new item entry
                    new_item = Item(title=item_data['title'], price=item_data['price'], image_url=item_data['image'])
                    db.session.add(new_item)
        
            # Commit changes to the database
            db.session.commit()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/remove-item', methods=['POST'])
def remove_item():
    try:
        data = request.get_json()
        item_id = data.get('id')
        # Find the item by ID
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            # Fetch items after removal
            items = Item.query.all()
            return jsonify({'success': True, 'items': [item.serialize() for item in items]})
        else:
            return jsonify({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/update-item-price', methods=['POST'])
def update_item_price():
    try:
        data = request.get_json()
        item_id = data.get('id')
        new_price = data.get('price')
        # Find the item by ID
        item = Item.query.get(item_id)
        if item:
            item.price = new_price
            db.session.commit()
            # Fetch items after update
            items = Item.query.all()
            return jsonify({'success': True, 'items': [item.serialize() for item in items]})
        else:
            return jsonify({'success': False, 'error': 'Item not found'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)



