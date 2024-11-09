comandos de django
==================
cargamos la tabla o models
---------------------------
```python
from django.db import models
```
creamos la clase o tabla
------------------------
```python
class Tabla(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.CharField(max_length=50)
    campo3 = models.CharField(max_length=50)
```
creamos la tabla en la base de datos
-------------------------------------
```python
python manage.py makemigrations
python manage.py migrate
```
```

```python
from django.db import models