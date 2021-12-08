
from re import escape
from lojas.amazon import *
from lojas.cultura import Cultura
from lojas.estantevirtual import *
from lojas.cultura import *
from lojas.saraiva import*
from lojas.travessa import*
'''amazon = Amazon()
amazon.searchBooks('tecnologia') #pode digitar tema

livros = amazon.getBooks()

print(livros)

estante = EstanteVirtual()
estante.searchBooks('dan brown')

livros1 = estante.getBooks()

print(livros1)
'''
cultura = Travessa()

cultura.searchBooks('dan brown')

livro = cultura.getBooks()
print(livro)
