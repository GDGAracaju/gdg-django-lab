#Publicando

Aplicações Django podem ser publicadas em:

- Seu próprio servidor
- Provedores
- Heroku
- Amazon AWS
- Google App Engine

~~sub-section~~

##Publicando no Heroku

Faça sua conta gratuita!

![Heroku](./img/heroku.png "Heroku")

~~sub-section~~

##Crie um app!

Enquanto cria um app no Heroku, vamos adaptar nosso projeto:

- Crie o arquivo `Procfile` na raiz do repositório:

```
web: gunicorn gdg_pizza.wsgi
```

Crie o arquivo `requirements.txt`:

```
Django==1.6
dj-database-url==0.2.2
dj-static==0.0.5
gunicorn==18.0
psycopg2==2.5.1
static==0.4
wsgiref==0.1.2
```

~~sub-section~~

Edite  as configurações de banco de dados no `settings.py`:

```python
(...)
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
(...)
```

Edite `wsgi.py`:

```python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gdg_pizza.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
```

~~sub-section~~

Adiciona sua chave SSH ao Heroku.

```bash
cat ~/.ssh/id_rsa.pub
```

![SSH](./img/ssh_key.png "SSH")

~~sub-section~~

O Heroku, por padrão, pede que sua aplicação esteja na pasta raiz do repositório.

Mova tudo dentro da pasta do projeto para a raiz.

E depois faça:

```bash
git remote add heroku ENDERECO_DO_SEU_REPO
git push heroku master
```

~~sub-section~~

##Virtualenv

É uma forma de isolar o ambiente de desenvolvimento Python.

Demonstração :-)

~~sub-section~~

Variável de ambiente para o banco de dados!

```bash
export DATABASE_URL=postgres://action@0.0.0.0/gdg_pizza
```