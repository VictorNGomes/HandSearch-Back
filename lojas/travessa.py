import requests
from bs4 import BeautifulSoup
import json
#from livro import Livro
import re
import string


class Travessa():
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
        r = requests.get('https://www.travessa.com.br/Busca.aspx?d=1&bt='+str(self.search)+'&cta=00&codtipoartigoexplosao=1&pag='+ str(self.no_page), headers=self.header)#, proxies=proxies)
        content = r.content
        self.soup = BeautifulSoup(content)

        self.dictLivros['search'] = search

    def getBooks(self):
        id =0
        for d in self.soup.findAll('table', attrs={'style':'border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:darkgrey;width:100%;'}):
            #print(d)
            try:
                name = d.find('a', attrs={'class':'buscaResultadoTitulo'})
                name = name.text
                name = string.capwords(name)
                name = re.split(' - ', name)
                name = name[0]


                #n = name.find_all('img', alt=True)
                #print(n[0]['alt'])
                author = d.find('span', attrs={'class':'buscaResultadoAutorProdutor'})
                #rating = d.find('span', attrs={'class':'4,1 de 5 estrelas'})
                #r = rating.find_all('span', aria-label=True)
                
                price = d.find('span', attrs={'class':'buscaResultadoPrecoPor'})
                price = price.text
                price = re.sub(r'Por:', '', price)

                imgUrl = d.find('img')['src']
                
                siteUrl = d.find('a')['href']
                
                self.dictLivros['Livros'].append({
                        'id':id,
                        'title': name,
                        'author': author.text,
                        'price': price,
                        'link': siteUrl,
                        'image':imgUrl
                    })

                id = id+1
            except:
                continue

        return self.dictLivros