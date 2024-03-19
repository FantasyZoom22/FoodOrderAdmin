from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://noureddine:yeZ1JYO0d9SqDdMyVL2BW14xSivEXm1G@dpg-cnsu8p5a73kc73b713u0-a:5432/itemsdb'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Create tables based on the defined models
db.create_all()

@app.route('/')
def index():
    # Fetch items from the database
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

@app.route('/update-items', methods=['POST'])
def update_items():
    # Get form data
    item_name = request.form['itemName']
    item_quantity = int(request.form['itemQuantity'])
    item_image_url = request.form['itemImage']
    
    # Create a new Item instance
    new_item = Item(name=item_name, quantity=item_quantity, image_url=item_image_url)
    
    # Add the new item to the database session
    db.session.add(new_item)
    db.session.commit()
    
    # Redirect back to the admin panel
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)
