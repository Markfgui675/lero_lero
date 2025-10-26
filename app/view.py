from flask import request, redirect, url_for, render_template
from app import app
from app import palavras

@app.route('/')
def index():
    return render_template('index.html')
