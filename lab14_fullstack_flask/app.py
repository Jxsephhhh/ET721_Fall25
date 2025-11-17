from flask import Flask, render_template, request
from flask_mysqldb import MySQL

# create a Flask object
app = Flask(__name__)

# connect to MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

# initialize MySQL
mysql = MySQL(app)

# route the data from the front-end
@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']

        # create cursor and execute query
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee(name, age) VALUES(%s, %s)", (name, age))

        # commit changes and close cursor
        mysql.connection.commit()
        cur.close()

        msg = "Data inserted successfully!"

    # render template for both GET and POST
    return render_template("index.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)