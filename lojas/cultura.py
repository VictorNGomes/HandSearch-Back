import requests
from bs4 import BeautifulSoup
import json
#from livro import Livro
import re
import string


class Cultura():
    def __init__(self):
        self.no_page = 1
        self.soup = None
        self.livros = []
        self.dictLivros = {'search':'', 'Livros':[]}

    def searchBooks(self,search):
        self.search = search.replace(" ", "+")
        self.header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
                        "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                        "DNT":"1",
                        "Connection":"close", 
                        "Upgrade-Insecure-Requests":"1"}
        r = requests.get('https://www3.livrariacultura.com.br/livros/?ft='+str(self.search)+'&originalText='+str(self.search)+'#' + str(self.no_page), headers=self.header)#, proxies=proxies)
        content = r.content
        self.soup = BeautifulSoup(content)

        self.dictLivros['search'] = search

    def getBooks(self):
        id = 0
        for d in self.soup.findAll('li', attrs={'class':'livros'}):
                #print(d)
                try:
                    name = d.find('h2', attrs={'class':'prateleiraProduto__informacao__nome'})
                    name = name.text
                    name = re.sub('\n','', name)
                    name = string.capwords(name)

                    #n = name.find_all('img', alt=True)
                    #print(n[0]['alt'])
                    author = d.find('li')
                    author = author.text
                    author = re.split(r'\|', author)
                    
                    for i in range(len(author)):
                        if re.search(r'Autor:', author[i]):
                            author = author[i]
                            break
                    author = re.sub(r'Autor:','', author)
                    author = re.split(r'\, ', author)
                    if len(author) >= 2:
                        author = author[1] + " " + author[0]
                    else:
                        author = author[0]
                    author = string.capwords(author)
                    #rating = d.find('span', attrs={'class':'4,1 de 5 estrelas'})
                    #r = rating.find_all('span', aria-label=True)
                    
                    price = d.find('span', attrs={'class':'prateleiraProduto__informacao__preco--valor'})

                    imgUrl = d.find('div', attrs={'class': 'prateleiraProduto__foto__content'}).find('template', attrs={'class':'foto__template__image'}).find('img')['src']
                    
                    siteUrl = d.find('h2', attrs={'class':'prateleiraProduto__informacao__nome'}).find('a')['href']

                    self.dictLivros['Livros'].append( {
                            'id':id,
                            'title': name,
                            'author': author,
                            'price': price.text,
                            'link': siteUrl,
                            'image':imgUrl
                            })
                    id = id+1
                except: 
                    continue

        return self.dictLivros 