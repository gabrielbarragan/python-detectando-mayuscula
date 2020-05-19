## Detectando mayúscula con Python

Define la función `find_upper` que recibe dos diccionarios como argumento y regresa otro diccionario, la clave del diccionario retornado será la primera letra del valor de la clave `last_name` de los otros dos diccionarios recibidos como argumentos, siempre y cuando este valor empiece con mayúsculas. 

Es importante desarrollar tu código usando `unittest` para verificar que tu programa se comporta y produce el resultado deseado.

```python
"""find_upper function"""

...

```

```python
"""Ejemplo de resultado"""

person1 = {"name": "candy", "last_name": "Feder", "age": 34}
person2 = {"name": "Manuel", "last_name": "martínes", "age": 21}

print(find_upper(person1, person2))
>> {'F': 'Feder'}



```

```
#unittest - TDD

$ python test_find_upper.py
```
