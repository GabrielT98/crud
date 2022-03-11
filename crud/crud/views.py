from doctest import testfile
from html import entities
from xml.dom.minidom import Entity
from django.shortcuts import render


from crud.entity import Produto
lista_produto = []
def listar_produto(request):
    produto1 = Produto()
    produto1.id = len(lista_produto)+1
    produto1.nome = "teste"
    produto1.descricao="test tets"
    lista_produto.append(produto1)

    return render(request,"index.html",{"produtos":lista_produto})


def ver_detalhes(request,id:int):
    for produto in lista_produto:
        if produto.id == id:
            return render(request,"produto.html",{"produto":produto})

