from flask import Flask, render_template, redirect, url_for, request
from os import path
import os

extra_dirs = ['static']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)

app = Flask(__name__)

#routers: page,

app.add_url_rule('/anggaran', 'anggaran', lambda : render_template('anggaran.html'))
app.add_url_rule('/anggaran-create-1', 'anggaran-create-1', lambda : render_template('anggaran-create-1.html'))
app.add_url_rule('/anggaran-create-2', 'anggaran-create-2', lambda : render_template('anggaran-create-2.html'))

app.add_url_rule('/prk', 'prk', lambda : render_template('prk.html'))
app.add_url_rule('/prk-add', 'prk-add', lambda : render_template('prk-add.html'))
app.add_url_rule('/prk-detail', 'prk-detail', lambda : render_template('prk-detail.html'))
app.add_url_rule('/prk-review', 'prk-review', lambda : render_template('prk-review.html'))

app.add_url_rule('/spk', 'spk', lambda : render_template('spk.html'))
app.add_url_rule('/spk-create', 'spk-create', lambda : render_template('spk-create.html'))
app.add_url_rule('/spk-read', 'spk-read', lambda : render_template('spk-read.html'))
app.add_url_rule('/status', 'status', lambda : render_template('status.html'))

app.add_url_rule('/pengalihan', 'pengalihan', lambda : render_template('pengalihan.html'))
app.add_url_rule('/pd-add', 'pd-add', lambda : render_template('pd-add.html'))
app.add_url_rule('/pd-detail', 'pd-detail', lambda : render_template('pd-detail.html'))
#
# @app.route('/', methods=['GET', 'POST'])
# def page():
#     page_name = request.args.get('page')
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return render_template(page_name+'.html', error=error)
#     return render_template(page_name+'.html', error=error)

app.run(host='127.0.0.1', port= 5000, extra_files=extra_files)