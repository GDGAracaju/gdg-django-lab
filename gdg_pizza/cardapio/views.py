#!/usr/bin/python
# coding: UTF-8
# Create your views here.
from django.http import HttpResponse

def cardapio_index(request):
    return HttpResponse("Olá! Bem vindo ao cardápio.")

def detail(request, category_id):
    return HttpResponse(u"Você está vendo detalhes da categoria %s." % category_id)

def products(request, category_id):
    return HttpResponse(u"Você está vendo a lista de produtos da categoria %s." % category_id)
