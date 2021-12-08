import requests
from bs4 import BeautifulSoup
import json
#from livro import Livro
import re

class EstanteVirtual():
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
        r = requests.get('https://www.estantevirtual.com.br/busca?q='+str(self.search)+'&livro_novo=1&offset='+str(self.no_page), headers=self.header)#, proxies=proxies)
        content = r.content
        self.soup = BeautifulSoup(content)

        self.dictLivros['search'] = search
    
    def getBooks(self):
        id = 0
        for d in self.soup.findAll('div', attrs={'class':'livro exibe-desagrupado'}):
            try:
                name = d.find('h2', attrs={'itemprop':'name'})
                name = name.text
                name = re.sub(r'\n|\n ', '', name)

            #n = name.find_all('img', alt=True)
            #print(n[0]['alt'])
                author = d.find('span', attrs={'itemprop':'author'} )
                author = author.text
                author = re.sub(r'\n|\n ', '', author)
                #rating = d.find('span', attrs={'class':'4,1 de 5 estrelas'})
                #r = rating.find_all('span', aria-label=True)
                
                price = d.find('span', attrs={'class':'preco'})

                imgUrl = d.find('div', attrs={'class': 'capa'}).find('img')['data-src']
                
                siteUrl = d.find('a', attrs={'class': 'livro-link js-ab-nvbbx'})['href']


                self.dictLivros['Livros'].append({
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