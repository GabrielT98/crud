from doctest import testfile
from html import entities
from xml.dom.minidom import Entity
from django.shortcuts import render



from crud.entity import Produto
lista_produto = []
"""
produto1 = Produto()
produto1.id = len(lista_produto)+1
produto1.nome = "teste"
produto1.descricao="test tsets"
lista_produto.append(produto1)
"""
def listar_produto(request):
    
    return render(request,"index.html",{"produtos":lista_produto})


def ver_detalhes(request,id:int):
    for produto in lista_produto:
        if produto.id == id:
            return render(request,"produto.html",{"produto":produto})

    return render(request,"404.html")
def adicionar_produto(request):
    if request.method == 'POST': 
        nome = request.POST['name']
        descricao = request.POST['descricao']
        valor = request.POST['valor']
        estoque = request.POST['estoque']
        produto = Produto()
        produto.id = len(lista_produto)+1
        produto.nome = nome
        produto.descricao = descricao
        produto.valor = valor
        produto.estoque = estoque
        lista_produto.append(produto)
        return render(request,"index.html",{"produtos":lista_produto})
    if request.method == 'GET':
        return render(request,"adicionar.html")

def delete_produto(request,id:int):
    for produto in lista_produto:
        if produto.id == id:
            lista_produto.remove(produto)
            return render(request,"index.html",{"produtos":lista_produto})
    return render(request,"404.html")