class Produto():
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__descricao = None
        self.__valor = None
        self.__qtd_estoque = None

    @property
    def id(self):
       return self.__id

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


    @property
    def valor(self):
       return self.__valor

    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor

    @property
    def estoque(self):
       return self.__qtd_estoque

    @estoque.setter
    def estoque(self, estoque:int):
        self.__qtd_estoque = estoque