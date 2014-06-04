#Web App

~~sub-section~~

##Criando um app

Django diferencia projeto de app:

- Um projeto pode conter vários apps.
- Apps podem ser reutilizados em outros projetos.

O que temos até agora é um projeto. Para criar um app:

```bash
./manage.py startapp cardapio
```

~~sub-section~~

##Estrutura de um app

- gdg_pizza
	- (...)
	- cardapio
		- \_\_init.py\_\_
		- models.py
		- tests.py
		- views.py

~~sub-section~~

##E o que são esses arquivos novos?

- **models.py**: Modelos/entidades que representam os dados do app.
- **tests.py**: Testes do app.
- **views.py**: Views do app.

~~sub-section~~

##models.py

```python
from django.db import models

class Product (models.Model)
	name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False, blank=True)
```

Ok, temos um modelo de produto. Nesse modelo, temos nome, preço, descrição e se ele é destaque ou não. Mas aonde vamos salvar os produtos?

~~sub-section~~

##Configurando o banco de dados

**Em sua máquina:**

- Instale o banco de dados de sua preferência
- Edite o settings.py

**No Nitrous.IO:**

```bash
parts install postgresql
```

Ou vá no menu `Autoparts -> Manage Packages`.

~~sub-section~~

##Django + PostgreSQL

Edite o arquivo `settings.py`:

```python
(...)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gdg_pizza',
        'HOST': '0.0.0.0',
        'PORT': '',
    }
}
(...)
```

Também existem os campos `USER` e `PASSWORD` que devem ser adicionados se necessário.

~~sub-section~~

##Adicionando nosso app ao projeto

Edite o arquivo `settings.py`:

```python
(...)
INSTALLED_APPS = (
    #Apps padrão do Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #E o nosso novo app também!
    'cardapio',
)
(...)
```

~~sub-section~~

##Mágica do SQL

```bash
python manage.py sql cardapio
```
```sql
BEGIN;
CREATE TABLE "cardapio_product" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "price" numeric(6, 2) NOT NULL,
    "description" text NOT NULL,
    "featured" boolean NOT NULL
)
;

COMMIT;
```

~~sub-section~~

##Outros comandos de banco de dados

```bash
python manage.py validate 			
python manage.py sqlclear cardapio
python manage.py syncdb				
```

- ```validate```: Valida os modelos do projeto.
- ```sqlclear```: Mostra os comandos DROP TABLE necessários para remover o app do banco de dados.
- ```syncdb```: Cria a estutura do projeto no banco de dados!

~~sub-section~~

##Mas e aí, pra manipular os dados?

```sql
INSERT INTO cardapio_product (name, price, description, featured) VALUES ('pizza', '20.0','uma pizza!',true);
```

~~sub-section~~

#\#NOT

~~sub-section~~

##Django Database API

Na verdade, você pode usar SQL personalizados.
Mas não precisa!

Vamos testar no shell do Django:

```bash
python manage.py shell
```

```python
from cardapio.models import Product
Product.objects.all()
c = Product(name='pizza',price=20.0,featured=True)
print(c.name)
c.save()
c.id
Product.objects.all()
```

~~sub-section~~

##Deixando os modelos mais intuitivos

Edite o seu `models.py`:

```python
(...)
class Product (models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField(blank=True)
	featured = models.BooleanField(default=False, blank=True)

	def __unicode__(self):
		return self.name
```

No shell do Django, faça:

```python
Product.objects.all()
```

~~sub-section~~

##Podemos alterar nosso modelo:

`models.py`
```python
import datetime

(...)
class Product (models.Model):
	
	(...)

	pub_date = models.DateTimeField('data de publicação')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	(...)
```

~~sub-section~~

##Mas e o banco de dados?

Ao alterar nosso modelo, o `syncdb` não atualiza a tabela. 

Podemos:

- Recriá-la ou alterá-la manualmente. (lembre do `./manage.py sql cardapio`)
- Usar um sistema de migrações, como o **South**.

~~sub-section~~

#Mas e o WebApp?

Calma!

~~sub-section~~

##Django Admin

Vamos editar nosso `settings.py`:

```python
(...)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'cardapio',
)
(...)
```

~~sub-section~~

E o `urls.py`:

```python
from django.conf.urls import patterns, include, url
import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

```

~~sub-section~~

E no terminal:

```bash
./manage.py syncdb
./manage.py runserver 0.0.0.0:8080
```

Agora abram o preview e adicionem `/admin` à URL :-)

~~sub-section~~

![Django Admin](./img/screen_django_admin.png "Django Admin")

~~sub-section~~

##E em PT-BR?

Editem o `settings.py`:
```python
(...)
TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'
(...)
```

~~sub-section~~

##Mas e o app Cardápio?

Crie um arquivo `admin.py` dentro do app:

```python
from django.contrib import admin
from cardapio.models import Product

admin.site.register(Product)
```

```bash
./manage.py runserver
```

![Django Admin](./img/screen_django_admin_ptbr.png "Django Admin")

~~sub-section~~

##Vamos deixar o `/admin` mais legível?

`models.py`

```python
# coding=UTF-8
(...)
class Product (models.Model):
    name = models.CharField('nome', max_length=100)
    price = models.DecimalField('preço', max_digits=6, decimal_places=2)
    description = models.TextField('descrição', blank=True)
    featured = models.BooleanField('destaque', default=False, blank=True)
    pub_date = models.DateTimeField('data de publicação', auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
(...)
```

~~sub-section~~

![Django Admin](./img/screen_django_admin_ptbr_2.png "Django Admin")

~~sub-section~~

##Pensem na quantidade de código que vocês não escreveram:

- SELECT, INSERT, UPDATE, DELETE
- Validação
- Autenticação
- URLs amigáveis

E o Admin pode ser personalizado!

~~sub-section~~

##Organizando os campos exibidos no formulário

Edite o `admin.py`:

```python
(...)
class ProductAdmin(admin.ModelAdmin):
    fields = ['featured', 'name','price']

admin.site.register(Product, ProductAdmin)
```

~~sub-section~~

##Organizando os campos em painéis

```python
(...)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['name', 'featured']}),
        ('Detalhes', {'fields': ['price', 'description']})
    ]
(...)
```

~~sub-section~~

##Adicionando mais modelos

Edite o `models.py`:

```python
(...)
class Category(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100,
                            help_text='O nome da categoria')
    created_on = models.DateTimeField(auto_now_add=True, 
                            verbose_name='Criado em')
    updated_on = models.DateTimeField(auto_now=True, 
                            verbose_name='Atualizado em')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

class Product (models.Model):
    category = models.ForeignKey(Category)
(...)
```

~~sub-section~~

E o `admin.py`:

```python
from django.contrib import admin
from cardapio.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['category', 'name', 'featured']}),
        ('Detalhes', {'fields': ['price', 'description']})
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
```

~~sub-section~~

##Atualize tudo!

```bash
 psql -c "drop database gdg_pizza;"
 psql -c "create database gdg_pizza;"

 ./manage.py syncdb
 ./manage.py runserver
```

E abra o Admin :-)

~~sub-section~~

##Adicionando Produtos e Categorias

Edite o `admin.py`:

```python
(...)
class ProductsInline(admin.StackedInline):
  model = Product
  extra = 2
  
class CategoryAdmin(admin.ModelAdmin):
  inlines = [ProductsInline]
(...)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
```

~~sub-section~~

![Django Admin](./img/screen_django_admin_ptbr_3.png "Django Admin")

~~sub-section~~

##Ordenando e filtrando no Admin

Edite o `admin.py`:

```python
(...)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'featured')
	list_filter = ['pub_date']
	search_fields = ['name', 'description']
(...)
```

E o `models.py`

```python
(...)
class Product (models.Model):
	category = models.ForeignKey(Category, verbose_name='Categoria')
(...)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Publicado recentemente?'
(...)
```

~~sub-section~~

![Django Admin](./img/screen_django_admin_ptbr_4.png "Django Admin")

~~sub-section~~

##Views

- Uma view é um tipo de página em seu projeto, que corresponde a uma função de sua aplicação.
- Cada página ou conteúdo no Django é servido como uma view.
- Cada view corresponde a uma função/método.
- O Django escolhe através da URL Conf.
- Nós já temos uma view!

~~sub-section~~

##Escrevendo views

Lembrem do `gdg_pizza\views.py`.

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
```

E do `urls.py`:

```python
from django.conf.urls import patterns, include, url
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
```

~~sub-section~~

##Criando uma view de um app

Dentro de `cardapio`, edite `views.py`:

```python
#encoding=utf-8
from django.http import HttpResponse

def cardapio_index(request):
    return HttpResponse("Olá! Bem vindo ao cardápio.")
```

E crie `urls.py`

```python
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.cardapio_index, name='cardapio_index')
)
```

~~sub-section~~

##Incluindo URLs de apps

Edite o `gdg_pizza\urls.py`:

```python
(...)
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^cardapio/', include('cardapio.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
```

Agora você pode acessar a URL `/cardapio` e quaisquer outras que adicionemos ao módulo `cardapio`!

~~sub-section~~

##Escrevendo mais views:

Adicione mais algumas linhas no `cardapio/views.py`:

```python
(...)
def detail(request, category_id):
    return HttpResponse(u"Você está vendo detalhes da categoria %s." \
						% category_id)

def products(request, category_id):
    return HttpResponse(u"Você está vendo a lista de produtos da categoria %s." \
						% category_id)

```

E o `cardapio/urls.py`:

```python
(...)
urlpatterns = patterns('',
    url(r'^$', views.cardapio_index, name='cardapio_index'),
	url(r'^(?P<category_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<category_id>\d+)/products/$', views.products, name='products'),
)
```

~~sub-section~~

##Views úteis!

`views.py`:

```python
def cardapio_index(request):
    #pega os últimos 5 registros de Categoria, ordenados por 'created_on'
    latest_category_list = Category.objects.order_by('-created_on')[:5]

    #junta todos os resultados da lista com ',' entre eles
    output = ', '.join([c.name for c in latest_category_list])

    return HttpResponse(output)
```

E acessem `/cardapio`.

~~sub-section~~

![Django Views](./img/screen_django_view_01.png "Django Views")

- Design misturado com código
- Difícil manutenção

~~sub-section~~

##Templates

- Reusabilidade de layout
- Personalização de apps
- Facilita a geração de HTMLs

~~sub-section~~

##Criando templates

Dentro de `cardapio`, crie a pasta `templates`.

Por padrão, o Django procura por templates em vários locais. Esse é um deles!

Crie o arquivo `index.html`:

```html
{% if latest_category_list %}
    <ul>
    {% for category in latest_category_list %}
        <li>
            <a href="/cardapio/{{ category.id }}/">{{ category.name }}</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>Nenhuma categoria disponível.</p>
{% endif %}
```

~~sub-section~~

##Usando templates nas views

Edite o seu `views.py`:

```python
from django.template import RequestContext, loader
(...)

def cardapio_index(request):
    template = loader.get_template('cardapio/index.html')
    latest_category_list = Category.objects.order_by('-created_on')[:5]
    context = RequestContext(request, {
        'latest_category_list': latest_category_list,
    })
    return HttpResponse(template.render(context))
```

~~sub-section~~

![Django Views](./img/screen_django_view_02.png "Django Views")

- Linguagem simplificada
- Existem algumas formas de controle:
    - `if`, `for`
    - `counters`
    - `includes`
- Fácil adaptação de layouts existentes

~~sub-section~~

##Atalho: `render()`

É muito comum usar `HttpResponse`, `loader`, `RequestContext`. 

Então o Django oferece um atalho:

`views.py`:

```python
(...)
from django.shortcuts import render

def cardapio_index(request):
    latest_category_list = Category.objects.order_by('-created_on')[:5]
    context = {'latest_category_list': latest_category_list}
    return render(request, 'cardapio/index.html', context)
(...)
```

~~sub-section~~

##Lançando um erro: 404

`views.py`:

```python
def detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'cardapio/detail.html', {'category': category})
```

Por enquanto, crie `templates\detail.html` apenas com:

```html
{{ category }}
```

~~sub-section~~

Válido:

![Django Views](./img/screen_django_view_03.png "Django Views")

Inválido:

![404](./img/screen_django_404.png "404")

~~sub-section~~

##Atalho: `get_object_or_404()`

Também é bem comum tentar pegar um objeto no banco de dados e lançar um erro caso não o encontre.

Então temos mais um atalho do Django!

Reescrevendo `views.py`:

```python
(...)
from django.shortcuts import render, get_object_or_404
(...)
def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'cardapio/detail.html', {'category': category})
(...)
```

~~sub-section~~

Reescrevendo o template `detail.html`:

```html
<h1>{{ category.name }}</h1>
<ul>
{% for p in category.product_set.all %}
    <li>{{ p.name }}</li>
{% endfor %}
</ul>
```

![Django Views](./img/screen_django_view_04.png "Django Views")

~~sub-section~~

