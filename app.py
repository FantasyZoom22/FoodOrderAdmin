from flask import Flask, render_template

app = Flask(__name__)

# Route for index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for admin_panel.html
@app.route('/admin-panel')
def admin_panel():
    return render_template('admin-panel.html')

if __name__ == '__main__':
    app.run(debug=True)
