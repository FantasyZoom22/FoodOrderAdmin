from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Replace 'username', 'password', 'host', 'port', and 'database_name' with your PostgreSQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://noureddine:yeZ1JYO0d9SqDdMyVL2BW14xSivEXm1G@dpg-cnsu8p5a73kc73b713u0-a

:5432/itemsdb'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Create the database tables (only need to do this once)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/update-items', methods=['POST'])
def update_items():
    item_name = request.form['itemName']
    item_quantity = int(request.form['itemQuantity'])
    item_image_url = request.form['itemImage']
    
    new_item = Item(name=item_name, quantity=item_quantity, image_url=item_image_url)
    db.session.add(new_item)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
