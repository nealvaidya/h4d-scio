from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import simplejson as json

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
df = df.assign(time = pd.to_datetime(df.time))
df = df.assign(ymd = df.time.apply(lambda x: x.strftime("%Y-%m-%d")))
df = df.set_index(df['time'])
df = df.sort_index()

def scio(keyword, start_date, end_date):
    ocurrences = df['tweets'].apply(lambda x: str.count(x.lower(),keyword.lower())>0)
    ocurrences_df = df.loc[ocurrences].drop('time', axis = 1)
    grouped_ocurrences_df = ocurrences_df.groupby('ymd')

    freq = []
    data = []
    daterange = pd.date_range(start_date, end_date).strftime("%Y-%m-%d")
    for single_date in daterange:
        if single_date not in grouped_ocurrences_df.groups:
                freq.append(0)
                data.append( {} )
        else: 
                group = grouped_ocurrences_df.get_group(single_date)
                freq.append(group.shape[0])
                data.append(group.to_dict('records'))
    return pd.DataFrame({
            'date': daterange, 
            'freq': freq,
            'data': data})

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('result.html')

@app.route('/result', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        result = request.form
        keyword = result.get('keyword').lower()
        similars = list(map(lambda x:x[0],
                        model.wv.most_similar(positive=keyword)))
        freqs = scio(keyword, '2016-01-01', '2016-5-12').to_dict(orient='records')
        return render_template("result.html", keyword=keyword, freqs=json.dumps(freqs,indent=2), similars=similars)

def get_all_ocurrences(keyword):
        ocurrences = df['tweets'].apply(lambda x: str.count(x.lower(),keyword)>0)
        ocurrences_df = df.loc[ocurrences].drop('time', axis = 1)

        ocurrences_nested_list = []
        for date,tweets in ocurrences_df.groupby('ymd'):
                ocurrences_nested_list.append( (date, tweets.to_dict('records')) )

        return ocurrences_nested_list


@app.route('/keyword', methods = ['GET'])
def new_word():
        keyword = request.args['word']
        return json.dumps(scio(keyword, '2016-01-01', '2016-5-12').to_dict(orient='records'), ignore_nan=True)

@app.route('/similars', methods = ['GET'])
def similar_word():
        keyword = request.args['word']
        similars = list(map(lambda x: x[0], model.wv.most_similar(positive=keyword)))
        return json.dumps(similars)

if __name__ == '__main__':
    app.run(debug=True)

