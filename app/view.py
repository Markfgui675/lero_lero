from flask import render_template
from app import app
from app.palavras import word
from random import randint
from dicio import Dicio

dicio = Dicio()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sortear')
def sortear():
    i = randint(0,71687)
    palavra = word(i)
    significado = dicio.search(palavra).meaning
    return render_template('sortear.html', palavra=palavra, significado=significado)

