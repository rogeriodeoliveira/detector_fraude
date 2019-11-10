from flask import render_template
from app import app

import pickle
import numpy as np
import pandas as pd
import nltk
import sklearn.feature_extraction
from flask import Flask, request, jsonify

from  app.models.vt import scan_url

# Lembre-se que você dever criar seu modelo e dicionário no Jupyter Notebook
# e salvar os arquivos na pasta notebook deste projeto
modelo = pickle.load(open('notebook/modelo.pk1','rb'))
modelo_messages_words = pickle.load(open('notebook/messages_words.pk1','rb'))

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

def predict_model(dados):

  dados = dados
  link = dados['link']
  texto = dados['texto']
  
  text_process = process_text_conteudo(texto)

  loaded_vectorizer = sklearn.feature_extraction.text.CountVectorizer(vocabulary=modelo_messages_words)

  predicao = modelo.predict(loaded_vectorizer.transform(text_process))
  resultado = predicao[0]

  urlscan = link

  if link != '':
    if resultado == 1 or scan_url(urlscan) == True:
      return render_template('fraude.html')
    elif resultado == 0 and scan_url(urlscan) == False:
      return render_template('notfraude.html')
  else:
    if resultado == 1:
      return render_template('fraude.html')
    elif resultado == 0:
      return render_template('notfraude.html')

def process_text_conteudo(conteudo):
  import unicodedata
  import string

  nopont = [char for char in conteudo if char not in string.punctuation]
  nopont = ''.join(nopont).lower()
  
  nopont = unicodedata.normalize('NFKD', nopont).encode('ASCII', 'ignore').decode('ASCII')

  clean_palavras = [palavra for palavra in nopont.split() if palavra not in stopwords]

  return clean_palavras
