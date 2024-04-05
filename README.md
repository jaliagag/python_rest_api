# Test Flask API REST

> [!IMPORTANT]  
> - Instalar las dependencias para que funcione la documentacion

Aplicacion desplegada en [pythonanywhere](https://www.pythonanywhere.com/); La url es `http://jaliagaent.pythonanywhere.com/`.

## Endpoints

- "/": home que devuelve un diccionario; no es como debe verse
  - "/?input=<texto ejemplo>": devolvera la cantidad de caracteres que tiene el texto ingresado
- "/health": ver el estado de la app
- "/ping": endpoint no desplegado; usado durante la demo
- "/docs": la documentacion

## query.py

Para ver "bien" la app, usar el archivo `query.py` (solo necesita la libreria `requests`); modificar la linea 6 con el texto que queremos "analizar" y correrlo.

```bash
$ python3 query.py
Le Input: this be a test
Datetime: 2024-04-04 21:56:21.010401
Character count: 14

```


