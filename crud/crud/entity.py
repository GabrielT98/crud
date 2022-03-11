class Produto():
    def __init__(self):
        self.__ = None
        self.__nome = None
        self.__descricao = None

    @property
    def id(self):
       return id.__nome

    @id.setter
    def id(self,id):
        self.__id = id 
    @property
    def nome(self):
       return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome 
    
    @property
    def descricao(self):
       return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao