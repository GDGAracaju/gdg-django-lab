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

Ao alterar nosso modelo, o `syncdb` não atualiza a tabela. 

Podemos:

- Recriá-la ou alterá-la manualmente. (lembre do `./manage.py sql cardapio`)
- Usar um sistema de migrações, como o **South**.

~~sub-section~~

