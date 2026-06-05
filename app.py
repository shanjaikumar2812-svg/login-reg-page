from flask import Flask, render_template, request, redirect
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "datascience"
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fullname']
        email = request.form['email']
        password = request.form['cpassword']
        cursor = db.cursor() 
        query = "INSERT INTO user (fullname,email,password) VALUES(%s,%s,%s)"
        values = (fname, email, password)
        cursor.execute(query, values)
        db.commit()
        cursor.close() 

        return redirect('/login')
    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST': 
        useremail = request.form['email']
        password = request.form['password']
        
        cursor = db.cursor()

        query = "SELECT * FROM user where email=%s AND password=%s"
        values = (useremail, password)
        cursor.execute(query, values)
        data = cursor.fetchone()
        cursor.close()
        
        if data:
            return "logged-in successfully"
        else:
            return "invalid email or password"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)