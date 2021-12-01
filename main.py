
from lojas.amazon import *

amazon = Amazon()
amazon.searchBooks('tecnologia') #pode digitar tema

livros = amazon.getBooks()

print(livros)