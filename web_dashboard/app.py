from flask import Flask, render_template, jsonify, request, redirect, session
import firebase_admin
from firebase_admin import credentials, db
import os

# Initialize Firebase
cred = credentials.Certificate("iot-attendance-system-914b1-firebase-adminsdk-fbsvc-c832ed67dc.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-attendance-system-914b1-default-rtdb.firebaseio.com//"
})

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['logged_in'] = True
            return redirect('/')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/data')
def data():
    attendance_ref = db.reference("attendance")
    attendance_data =  attendance_ref.get()
    return jsonify(attendance_data)


if __name__ == "__main__":
    app.run(debug=True)

