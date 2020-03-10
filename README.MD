
  

# Detector de Fraude

  


Esta aplicação tem como objetivo analisar textos de e-mail ou SMS ou outros para identificar uma mensagem fraudulenta.

A aplicação foi desenvolvida utilizando Python - Flask e IA.


Uso Real  [https://rogeriodeoliveira.com/analisador-fraude](https://rogeriodeoliveira.com/analisador-fraude) 

Esta aplicação utiliza Inteligência Artificial (Machine Learnig) para classificar textos como **Fraude** e **Não-Fraude**.

  

  

![inicial](https://github.com/rogeriodeoliveira/flask_api_ai_fraud/blob/master/tela_inicial.png)

  

  

![fraude](https://github.com/rogeriodeoliveira/flask_api_ai_fraud/blob/master/tela_fraude.png)

  

  

![n_fraude](https://github.com/rogeriodeoliveira/flask_api_ai_fraud/blob/master/tela_n_fraude.png)

  

  

Vídeo: [Demo](https://youtu.be/Qw4TNMLDzC0)

  

O modelo de classificação foi feito utilizando o Jupyter notebook, ele esta disponível na pasta [notebook](https://github.com/rogeriodeoliveira/detector_fraude/blob/master/notebook/Fraud_Detect.ipynb)

  

Este modelo trabalha com 2 datasets, um contendo e-mails classificados como fraudulentos e o segundo deverá conter e-mail não fraudulentos.

O **primeiro dataset** você pode fazer o download dele [aqui](https://github.com/rogeriodeoliveira/scrapy_fraudes_rnp/blob/master/dataset_fraudes.csv)

O **segundo dataset** foi criado a partir de mensagens pessoais, então eu não vou disponibilizar este dataset, porém eu também estou disponibilizando um script para gerar este dataset para treinamento deste modelo. Você pode acessá-lo no repositório [gerador_dataset](https://github.com/rogeriodeoliveira/gerador_dataset) juntamente com um pequeno tutorial de como eu fiz para exportar os e-mails.
