import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='finance-tracker-db.cxgyq42qqfm5.ap-southeast-2.rds.amazonaws.com', 
        user='jinnyfirst',
        password='Jinny5527024!',
        database='financetracker'
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM expenses')
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
