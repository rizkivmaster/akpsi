from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/', defaults={'path': 'Dashboard.html'})
@app.route('/<path:path>', methods=['GET', 'POST'])
def home(path):
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('Dashboard.html', error=error)
    return render_template(path, error=error)

app.run(host='0.0.0.0', port= 5000)