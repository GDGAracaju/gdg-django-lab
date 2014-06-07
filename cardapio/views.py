#!/usr/bin/python
# coding: UTF-8
# Create your views here.
from cardapio.models import Category
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

def cardapio_index(request):
    latest_category_list = Category.objects.order_by('name')
    context = {'latest_category_list': latest_category_list}
    return render(request, 'cardapio/index.html', context)

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'cardapio/detail.html', {'category': category})

def add(request):
    return render(request, 'cardapio/add.html')

def add_category(request):
	c = Category()
	try:
		c.name = request.POST['category']
		c.save()
	except:
		return render(request, 'cardapio/add.html', { 'error_message': 'Algo errado :-(' })
	return HttpResponseRedirect(reverse('cardapio:cardapio_index'))