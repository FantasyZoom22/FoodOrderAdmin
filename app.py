from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="itemsdb",
    user="noureddine",
    password="yeZ1JYO0d9SqDdMyVL2BW14xSivEXm1G",
    host="dpg-cnsu8p5a73kc73b713u0-a"
)
cur = conn.cursor()

# Route to display items on index.html
@app.route('/')
def index():
    # Fetch items from the database
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    return render_template('index.html', items=items)

# Route to display admin panel
@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

# Route to handle form submission from admin-panel.html
@app.route('/add-item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        # Get form data
        name = request.form['itemName']
        price = request.form['itemPrice']
        image_url = request.form['itemImage']
        
        # Insert data into the database
        cur.execute("INSERT INTO items (name, price, image_url) VALUES (%s, %s, %s)", (name, price, image_url))
        conn.commit()
        
    # Redirect to the index route after adding item
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
