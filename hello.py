from flask import Flask
from flask import render_template
from flask import request

import pandas as pd
import gensim
import logging

# text_corpus = []
# for i,line in enumerate(data.iloc[:,5])

app = Flask(__name__)



@app.route('/')
def my_form():
    return render_template('index2.html')

@app.route('/result', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)

