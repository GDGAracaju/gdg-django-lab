#Aprimorando

- HTML 5
- Layout
- Templates
- Javascript
- CSS
- Responsividade

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