import requests
from bs4 import BeautifulSoup
import json
#from livro import Livro
import re

class Saraiva():
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
        r = requests.get('https://busca.saraiva.com.br/busca?q='+str(self.search)+'&page='+ str(self.no_page), headers=self.header)#, proxies=proxies)
        content = r.content
        self.soup = BeautifulSoup(content)

        self.dictLivros['search'] = search

    def getBooks(self):
        id =0
        for d in self.soup.findAll('li', attrs={'class':'nm-product-item'}):
            #print(d)
            name = d.find('a', attrs={'class':'nm-product-name'})
            #n = name.find_all('img', alt=True)
            #print(n[0]['alt'])
            author = d.find('div', attrs={'class':'nm-product-sub'})
            try:
                author = author.text
                author = re.sub("\n| ","", author)
                author = re.split(',', author)
                if len(author) >= 2:
                    author = author[1] + " " + author[0]
                else:
                    author = author[0]
            except:
                continue
            #print(author)
            #rating = d.find('span', attrs={'class':'4,1 de 5 estrelas'})
            #r = rating.find_all('span', aria-label=True)
            
            price = d.find('div', attrs={'class':'nm-price-container'})
            try:
                price = price.text
                price = re.sub("\n| ", "", price)
                price = re.split('\$', price)
                price = "R$ " + price[1]
            except:
                break

            imgUrl = d.find('img', attrs={'class': 'nm-product-img'})['src']
            
            siteUrl = d.find('a', attrs={'class': 'nm-product-img-link'})['href']

            self.dictLivros['Livros'].append({
                    'id':id,
                    'title': name.text,
                    'author': author,
                    'price': price,
                    'link': siteUrl,
                    'image':imgUrl
                })

            id = id+1

        return self.dictLivros