#Aprimorando

- HTML 5
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

Então, vamos usá-lo! Crie uma pasta `static` dentro do projeto.

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

Agora, vamos criar `base.html` na nossa pasta de templates:

```html

```

~~sub-section~~

##Template do Admin

Edite o `settings.py`:

```python
(...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates')
)
(...)
```