from os import name
from flask import Flask
import flask
from lojas.amazon import *
from flask import jsonify
from markupsafe import escape


app = Flask(__name__)

@app.get('/amazon/<name>')
def search(name):
    amazon = Amazon()
    url = escape(name)
    amazon.searchBooks(str(url))
    livros = amazon.getBooks()
    return livros
app.run()





