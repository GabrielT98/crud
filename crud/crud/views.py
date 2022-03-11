from doctest import testfile
from html import entities
from xml.dom.minidom import Entity
from django.shortcuts import render


from crud.entity import Produto

def listar_produto(request):
    lista_produto = []
    produto1 = Produto()
    produto1.id = len(lista_produto)+1
    produto1.nome = "teste"
    produto1.descricao="test tets"
    lista_produto.append(produto1)

    return render(request,"index.html",{"produtos":lista_produto})