from flask import Flask, render_template, request, redirect
from Main import Recommendations as re
import os
import pymorphy2
import sqlite3
from nltk.corpus import stopwords
import sqlite3

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main_page():
    return render_template('layout.html')


img = os.path.join('../static', 'flower_img')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        user_msg = request.form['assistant__user-query']
        request_result = re.result_recommendation(user_msg)
        img_url = request_result[0][3]
        file = os.path.join(img, img_url)
        request_result_title = {
            'title' : f'{request_result[0][0]}'}
        request_result_description = {
            'description' : f'{request_result[0][1]}'}
        return render_template('data.html',  value1=request_result_title, value2=request_result_description, image=file)

nostring = "render_template('data.html',  form_data=form_data) "

if __name__ == '__main__':
   app.run(debug=True)