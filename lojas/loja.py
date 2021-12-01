import abc

class Loja(abc.ABC):

    @abc.abstractmethod
    def searchBooks():
        pass

    @abc.abstractmethod
    def getBooks():
        pass
        
