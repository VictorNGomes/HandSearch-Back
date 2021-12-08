from os import name
from flask import Flask
import flask
from lojas.amazon import *
from flask import jsonify
from markupsafe import escape
from lojas.estantevirtual import *
from lojas.estantevirtual import EstanteVirtual
from lojas.cultura import *
from lojas.saraiva import Saraiva
from lojas.travessa import Travessa
from flask_cors import CORS, cross_origin


app = Flask(__name__)

@app.route('/amazon/<name>', methods=['GET', 'POST'])
@cross_origin()
def search(name):
    amazon = Amazon()
    url = escape(name)
    amazon.searchBooks(str(url))
    livros = amazon.getBooks()
    return livros

@app.route('/estantevirtual/<name>',methods=['GET', 'POST'])
@cross_origin()
def searchEstante(name):
    e = EstanteVirtual()
    url = escape(name)
    e.searchBooks(str(url))
    livros = e.getBooks()
    return livros

@app.route('/cultura/<name>',methods=['GET', 'POST'])
@cross_origin()
def searchCult(name):
    c = Cultura()
    url = escape(name)
    c.searchBooks(str(url))
    livros = c.getBooks()
    return livros

@app.route('/saraiva/<name>',methods=['GET', 'POST'])
@cross_origin()
def searchSaraiva(name):
    s = Saraiva()
    url = escape(name)
    s.searchBooks(str(url))
    livros = s.getBooks()
    return livros

@app.route('/travessa/<name>',methods=['GET', 'POST'])
@cross_origin()
def searchTravessa(name):
    t = Travessa()
    url = escape(name)
    t.searchBooks(str(url))
    livros = t.getBooks()
    return livros



if __name__ == "__main__":
    app.run(debug = True)



