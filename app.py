import numpy as np
from flask import Flask, request, jsonify
import pickle
import os
import pandas as pd
import nltk
import sklearn.feature_extraction

app = Flask(__name__)

modelo = pickle.load(open('notebook/messages_words.pk1','rb'))
modelo_messages_words = pickle.load(open('notebook/messages_words.pk1','rb'))

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')


@app.route("/")
def verifica_api_online():
  return "API ONLINE v1.0", 200

@app.route('/predict', methods=['POST'])
def predict():

  dados = request.get_json(force=True)
  
  text_process = process_text_conteudo(dados.values())

  loaded_vectorizer = sklearn.feature_extraction.text.CountVectorizer(vocabulary=modelo_messages_words)

  predicao = modelo.predict(loaded_vectorizer.transform(text_process))
  resultado = predicao[0]
  resposta = {'FRAUDE': int(resultado)}
  
  return jsonify(resposta)

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


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(debug = True, host='0.0.0.0', port=port)