from flask import flask, render_template, request
from flask_mysqldb import flask_mysqldb

# Create a Flask Object
app = Flask(__name__)

# Connect to MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

mysq; = MySQL(app)

# Route the data from the front-end
@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO employee(name,age) VALUES(%s, %s)", (name, age))

        mysql.connection.commit()
        cur.close()

        msg = "Data successfully sent!"
    
    return render_template("index.html", msg = msg)

if __name__ == "__main__":
    app.run(debug = True)