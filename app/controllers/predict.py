from flask import render_template
from app import app

from flask import Flask, request, jsonify

from  app.models.predict import predict_model


@app.route('/resultado', methods=['POST'])
def predict():
  dados = request.form.to_dict()
  return predict_model(dados)
  