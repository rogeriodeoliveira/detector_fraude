from flask import render_template
from app import app

from app.models.forms import TextSubmit

@app.route("/", methods=["GET"])
def index():
  form = TextSubmit()

  if form.validate_on_submit():
    print(form.texto.data)
  return render_template('index.html', form=form)