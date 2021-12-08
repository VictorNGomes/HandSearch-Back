import requests
from bs4 import BeautifulSoup
import json
#from livro import Livro
#from lojas.loja import *


class Amazon():
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
        r = requests.get('https://www.amazon.com.br/s?k='+str(self.search)+'&i=stripbooks&page='+str(self.no_page)+'&__mk_pt_BR=?ref=sr_pg_'+str(self.no_page), headers=self.header)#, proxies=proxies)
        content = r.content
        self.soup = BeautifulSoup(content)

        self.dictLivros['search'] = search

    def printSoup(self):
        return print(self.soup);

    def getBooks(self):
        id = 0
        for d in self.soup.findAll('div', attrs={'class':'s-include-content-margin s-latency-cf-section s-border-bottom s-border-top'}):
           
            name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
            author = d.find_all('span', attrs={'class':'a-size-base'})

            if len(author) >= 4:
                author = author[3]
            else:
                author = author[1]

            price = d.find('span', attrs={'class':'a-offscreen'})
            imgUrl = d.find('img', attrs={'class': 's-image'})['src']
        
            siteUrl = "www.amazon.com.br"
            siteUrl += d.find('a', attrs={'class': 'a-link-normal s-no-outline'})['href']
            

            #livro = Livro(name,author,price)
            #self.livros.append(livro)


            self.dictLivros['Livros'].append( {
                    'id':id,
                    'title': name.text,
                    'author': author.text,
                    'price': price.text,
                    'link': siteUrl,
                    'image':imgUrl
                    })

            id = id+1
            
        return self.dictLivros

    def printJson(self):
       return json.dumps(self.dictLivros,sort_keys=False).encode('utf8')


 

    

        #print("Link: ",link['href'])
    


       


    






        





