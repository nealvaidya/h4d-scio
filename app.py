from flask import Flask
from flask import render_template
from flask import request
import json

import pandas as pd
import gensim
import logging
import matplotlib as plt
import numpy as np

data = pd.read_csv('static/tweets.csv', delimiter=',')
text_corpus = []
for i,line in enumerate(data.iloc[:,7]):
        text_corpus.append(gensim.utils.simple_preprocess(str(line)
        .replace("ENGLISH TRANSLATION: ","")))
model = gensim.models.Word2Vec(text_corpus, size = 148, window=10, min_count= 2, workers=10)
model.train(text_corpus,total_examples=len(text_corpus),epochs=10)

df = data
df['time']=pd.to_datetime(df['time'])
df = df.set_index(df['time'])
df = df.sort_index()

def scio(keyword, start_date, end_date):
    daterange = pd.date_range(start_date, end_date)
    
    freq = []
    for single_date in daterange:
                freq.append(' '.join(df[single_date.strftime("%Y-%m-%d"):single_date.strftime("%Y-%m-%d")].iloc[:,7].values).lower().count(keyword))
    return pd.DataFrame({
            'date': daterange.strftime("%Y-%m-%d").tolist(), 
            'freq': freq})

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index2.html')

@app.route('/result', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        result = request.form
        keyword = result.get('keyword').lower()
        similars = list(map(lambda x:x[0],
                        model.wv.most_similar(positive=keyword)))
        freqs = scio(keyword, '2016-01-01', '2016-5-12').to_dict(orient='records')
        return render_template("result.html",result='success', freqs=json.dumps(freqs,indent=2), similars=similars)

if __name__ == '__main__':
    app.run(debug=True)

