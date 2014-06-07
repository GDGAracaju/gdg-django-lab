from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('cardapio.urls', namespace='cardapio')),
    # Examples:
    # url(r'^$', 'gdg_pizza.views.home', name='home'),
    # url(r'^gdg_pizza/', include('gdg_pizza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
