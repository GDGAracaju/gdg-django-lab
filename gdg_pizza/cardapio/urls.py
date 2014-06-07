#encoding=utf-8
from django.conf.urls import patterns, url
from cardapio import views

urlpatterns = patterns('',
    url(r'^$', views.cardapio_index, name='cardapio_index'),
	url(r'^(?P<category_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add, name='add'),
	url(r'^add_category/$', views.add_category, name='add_category')
)
