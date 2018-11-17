from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('dashboard.html', error=error)
    return render_template('login.html', error=error)

app.run(host='127.0.0.1', port= 5000)