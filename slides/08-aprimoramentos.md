#Aprimorando

- Layout
- Templates
- Javascript
- CSS
- Responsividade

~~sub-section~~

##Arquivos estáticos

Em `settings.py` já temos a configuração de arquivos estáticos:

```python
STATIC_URL = '/static/'
```

Então, vamos usá-lo! Crie uma pasta `static` dentro do app `gdg_pizza`.

~~sub-section~~

##Bootstrap

Podemos alterar o nosso layout para usar o [Bootstrap](http://getbootstrap.com/).

Ele é um framework de front-end bastante popular, capaz de criar páginas responsivas e pensadas para mobile.

Acesse o [site](http://getbootstrap.com/) e baixe o arquivo compactado.

~~sub-section~~

##Bootstrap

Dentro do arquivo, você encontrará a versão compilada:

- bootstrap-x.y.z-dist
	- css: 
		Arquivos CSS e CSS minimizados
	- fonts: 
		Fontes utilizadas por padrão
	- js: 
		Arquivos Javascript

~~sub-section~~

##Página HTML com Bootstrap

Precisamos de alguns detalhes:

No head: 

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet">
```

No body:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js">
<script src="js/bootstrap.min.js">
```

Lembrem de fechar as tags `script`.

~~sub-section~~

##Bootstrap + Django

Vamos adaptar nosso template!

Primeiro, copie as pastas do Bootstrap para `static`.

Agora, vamos criar `base.html` na nossa pasta de templates. 

Dêem uma [olhada neste template](http://getbootstrap.com/examples/jumbotron/), fornecido pelo Bootstrap.

~~sub-section~~

Copie e cole o código do template no `base.html` e depois edite:

```html
(...)
<title>{% block title %}Jumbotron Template for Bootstrap{% endblock %}</title>
<link href="{% static "css/bootstrap.min.css" %}" rel="stylesheet">
(...)
<div class="container">

      {% block content %}
(...)
{% endblock %}

      <hr>

      <footer>
        <p>&copy; Company 2014</p>
      </footer>
(...)
<script src="{% static "js/bootstrap.min.js" %}"></script>
(...)
```

~~sub-section~~

##Herança de templates

Vamos usar nosso novo template nos outros!

`index.html`

```html
{% extends "cardapio/base.html" %}

{% block content %}
	{% if latest_category_list %}
	    <ul>
	    {% for category in latest_category_list %}
	        <li><a href="{% url 'cardapio:detail' category.id %}">{{ category.name }}</a></li>
	    {% endfor %}
	    </ul>
	{% else %}
	    <p>Nenhuma categoria disponível.</p>
	{% endif %}
{% endblock %}
```

~~sub-section~~

`detail.html`

```html
{% extends "cardapio/base.html" %}

{% block content %}
	<h1>{{ category.name }}</h1>
	<ul>
	{% for p in category.product_set.all %}
	    <li>{{ p.name }}</li>
	{% endfor %}
	</ul>
{% endblock %}
```

Agora rode a aplicação e veja a diferença!

~~sub-section~~

##Vamos melhorar!

Edite o `base.html`:

````html
(...)
<div class="jumbotron">
  <div class="container">
    <h1>{% block jumbo %} {% endblock %}</h1>
    {% block below_jumbo %}
    {% endblock %}
  </div>
</div>
(...)
```

~~sub-section~~

E o `detail.html`

```html
{% extends "cardapio/base.html" %}

{% block jumbo %}
	{{ category.name }}
{% endblock %}

{% block below_jumbo %}
	<a href="{% url 'cardapio:cardapio_index' %}">Voltar</a>
{% endblock %}

{% block content %}
	<ul>
	{% for p in category.product_set.all %}
	    <li>{{ p.name }}</li>
	{% endfor %}
	</ul>
{% endblock %}
```

~~sub-section~~

Antes de rodar, altere também o `views.py`:

```python
(...)
def cardapio_index(request):
    latest_category_list = Category.objects.order_by('name')
(...)
```

E `runserver`!

~~sub-section~~

##E a responsividade?

Edite o `index.html`:

```html
{% extends "cardapio/base.html" %}

{% block jumbo %}
	GDG Pizza!
{% endblock %}

{% block below_jumbo %}
	<p>Escolha uma categoria</p>
{% endblock %}

{% block content %}
	<div class="row">
	{% if latest_category_list %}
	    
	    {% for category in latest_category_list %}
	        <div class="col-md-4">
	        	<h2><a href="{% url 'cardapio:detail' category.id %}">{{ category.name }}</a></h2>
	        </div>
	    {% endfor %}
	    
	{% else %}
		<div class="col-md-4">
	    	<p>Nenhuma categoria disponível.</p>
	    </div>
	{% endif %}
	</div>
{% endblock %}
```

Teste!

~~sub-section~~

Vamos seguir a mesma filosofia com o `detail.html`:

```html
{% extends "cardapio/base.html" %}

{% block jumbo %}
	{{ category.name }}
{% endblock %}

{% block below_jumbo %}
	<a href="{% url 'cardapio:cardapio_index' %}">Voltar</a>
{% endblock %}

{% block content %}
	<div class="row">
	{% for p in category.product_set.all %}
	    <div class="col-md-4">
	    	<h2>{{ p.name }}</h2>
	    </div>
	{% endfor %}
	</div>
{% endblock %}
```

Experimente colocar imagens depois :-)

~~sub-section~~

##Adicionando um form

Vamos criar o template `add.html`:

```html
{% extends "cardapio/base.html" %}

{% block jumbo %}
Adiciona categoria
{% endblock %}

{% block content %}

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form role="form" action="{% url 'cardapio:add_category' %}" method="post">
{% csrf_token %}
    <div class="form-group">
    	<label for="category">Nome</label>
    	<input type="text"  name="category" id="category" value="" class="form-control"/>
    </div>
    
	<input type="submit" value="Adiciona" class="btn btn-default"/>
</form>

{% endblock %}
```

~~sub-section~~

E edite o `urls.py`:

```python
(...)
urlpatterns = patterns('',
    url(r'^$', views.cardapio_index, name='cardapio_index'),
	url(r'^(?P<category_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add, name='add'),
	url(r'^add_category/$', views.add_category, name='add_category')
)
```

E o `views.py`:

```python
(...)
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
```

~~sub-section~~

##Quer mais?

Sugestões para estudos:

- [Views genéricas](https://docs.djangoproject.com/en/1.6/intro/tutorial04/)
- [Django Forms](https://docs.djangoproject.com/en/1.6/topics/class-based-views/generic-editing/)
- [Autenticação](https://docs.djangoproject.com/en/1.6/topics/auth/)
- [Personalização do Admin](https://docs.djangoproject.com/en/1.6/ref/contrib/admin/)
- [Template do Admin](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates)
- [Apps de terceiros](https://github.com/search?q=django&ref=cmdform)
- [Testes automatizados](https://docs.djangoproject.com/en/1.6/intro/tutorial05/)
- [South](http://south.aeracode.org/)