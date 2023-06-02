from flask import Flask, render_template, request, redirect
from Main import Recommendations as re
import pymorphy2
import sqlite3
from nltk.corpus import stopwords
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main_page():
    return render_template('layout.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form['assistant__user-query']
        form_data = re.result_recommendation(form_data)
        return f"{form_data}"

nostring = "render_template('data.html',  form_data=form_data) "

if __name__ == '__main__':
   app.run(debug=True)