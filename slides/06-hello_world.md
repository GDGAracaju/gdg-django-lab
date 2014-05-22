#Hello Django

Vá ao terminal:

```bash
#Entrar na pasta do projeto:
cd ~/workspace/gdg-django-lab
#git checkout v-1
#git clean -f -d
django-admin.py startproject gdg_pizza
```

Projeto criado :-)

~~sub-section~~

##Estrutura básica do projeto

- gdg_pizza
	- manage.py
	- gdg_pizza
		- \_\_init\_\_.py
		- settings.py
		- urls.py
		- wsgi.py
    
~~sub-section~~

##O que são essas pastas e arquivos?

- **gdg_pizza**: essa pasta exterior é o diretório raiz do projeto. Seu nome não importa ao Django.
  - **manage.py**: utilitário de linha de comando que lhe permite interagir com seu projeto.

~~sub-section~~

##Mas e os outros?

- **gdg_pizza**: essa pasta interior é o pacote Python de seu projeto.
  - **\_\_init\_\_.py**: apenas um arquivo vazio para que o Python considere a pasta como um pacote Python.
  - **settings.py**: configurações de seu projeto Django.
  - **urls.py**: declarações de URLs para esse projeto Django.
  - **wsgi.py**: ponto de entrada para servidores web compatíveis com WSGI.

~~sub-section~~

##Servidor de desenvolvimento

Experimente executar no terminal:

```bash
python manage.py runserver 0.0.0.0:8080
```

Seu projeto Django já está rodando!

Para acessá-lo no Nitrous: menu ```Preview -> Port 8080```

~~sub-section~~

##runserver

```bash
Validating models...                                                                                                                                                                                     
                                                                                                                                                                                                         
0 errors found                                                                                                                                                                                           
May 20, 2014 - 22:10:47                                                                                                                                                                                  
Django version 1.5.1, using settings 'gdg_pizza.settings'                                                                                                                                                
Development server is running at http://127.0.0.1:8080/                                                                                                                                                  
Quit the server with CONTROL-C.
```

~~sub-section~~

##Seu primeiro projeto Django

![Django](./img/screen_django_01.png "Django")

~~sub-section~~

##runserver

- Você não precisa especificar a porta: por padrão é a 8000.
- Você não precisa especificar o IP: por padrão aceita apenas localhost!
- Não é necessário atualizar: alterações do código são recarregadas automaticamente.
- Não use em produção: servidor **apenas** para ambientes de desenvolvimento.

~~sub-section~~

##Adicionando uma página simples (1)

Edite o arquivo ```gdg_pizza\urls.py``` para incluir:

```python
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

```

~~sub-section~~

##Adicionando uma página simples (2)

Adicione o arquivo ```gdg_pizza\views.py``` com o código:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
```

~~sub-section~~

#Hello World!

![Django](./img/screen_django_02.png "Django")

~~sub-section~~

##Request Handlers

São os responsáveis por tratar as requisições HTTP.

Podem retornar HttpResponse, do pacote:
```python
from django.http import HttpResponse
```

E podem ser escritos da forma:
```python
def index(request):
    return HttpResponse("Hello, world. You're at the index.")
```

~~sub-section~~

##URL Conf

> ["Cool URIs don't change"](http://www.w3.org/Provider/Style/URI), Tim Berners-Lee

- URLs devem ser configuráveis
- URLs não precisam mudar: estabilidade

~~sub-section~~

##URL Conf

A configuração das URLs em Django podem ser feitas usando expressões regulares:
```python
urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
```
~~sub-section~~

##URL Patterns

```python
url(r'^$', views.index, name='index')
```

- `url()`: método gerador da URL.
- `r'^$'`: expressão regular para identificar a URL.
- `views.index`: método que tratará desse endereço.
- `name='index'`: nome da URL.

~~sub-section~~

##Expressões regulares

- `r`: indica que a string não deve ter caracteres escapados.
- `^`: começo da string.
- `$`: fim da string.

Então, `r'^$'` indentifica uma URL vazia! 

Note: as URLs do Django já consideram o endereço básico da aplicação!