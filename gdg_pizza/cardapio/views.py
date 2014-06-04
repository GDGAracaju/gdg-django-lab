#!/usr/bin/python
# coding: UTF-8
# Create your views here.
from cardapio.models import Category
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def cardapio_index(request):
    latest_category_list = Category.objects.order_by('-created_on')[:5]
    context = {'latest_category_list': latest_category_list}
    return render(request, 'cardapio/index.html', context)

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'cardapio/detail.html', {'category': category})
