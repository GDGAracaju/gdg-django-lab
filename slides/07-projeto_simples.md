#Web App

- HTML 5
- Layout
- Templates
- Javascript
- CSS
- Responsividade

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