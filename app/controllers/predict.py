from flask import render_template
from app import app

import pickle
import numpy as np
import pandas as pd
import nltk
import sklearn.feature_extraction
from flask import Flask, request, jsonify

modelo = pickle.load(open('notebook/modelo.pk1','rb'))
modelo_messages_words = pickle.load(open('notebook/messages_words.pk1','rb'))

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')


@app.route('/predict', methods=['POST'])
def predict():

  dados = request.form.to_dict()
  dados = dados['texto']
  
  text_process = process_text_conteudo(dados)

  loaded_vectorizer = sklearn.feature_extraction.text.CountVectorizer(vocabulary=modelo_messages_words)

  predicao = modelo.predict(loaded_vectorizer.transform(text_process))
  resultado = predicao[0]
  #resposta = {'FRAUDE': int(resultado)}
  if resultado == 1:
    return render_template('fraude.html')
  elif resultado == 0:
    return render_template('notfraude.html')

  #return jsonify(resposta)

def process_text_conteudo(conteudo):
  import unicodedata
  import string
  # Remove pontuação
  nopont = [char for char in conteudo if char not in string.punctuation]
  nopont = ''.join(nopont).lower()
  
  nopont = unicodedata.normalize('NFKD', nopont).encode('ASCII', 'ignore').decode('ASCII')

  # cria lista contendo somente palavras
  clean_palavras = [palavra for palavra in nopont.split() if palavra not in stopwords]

  return clean_palavras