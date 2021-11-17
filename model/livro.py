


class Livro:
    def __init__(self,title,author,price):
        self.title   = title
        self.author  = author
        self.price   = price

    def get_Title(self):
        return self.title.text
    def get_Author(self):
        return self.author.text
    def get_Price(self):
        return self.price.text