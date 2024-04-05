# Test Flask API REST

> [!IMPORTANT]  
> - Para correr la app localmente, asegurarse de instalar las dependencias para que funcione correctamente la documentacion

Aplicacion desplegada en [pythonanywhere](https://www.pythonanywhere.com/); La url es `http://jaliagaent.pythonanywhere.com/`.

## Test deployment

[video test](https://youtu.be/fCM5rK_Rqls)

## Runme

Para levantar la app localmente:

```bash
git clone git@github.com:jaliagag/python_rest_api.git
# (opcional) crear entorno virtual
python3 -m venv virtual
source virtual/bin/activate

cd app
pip3 install -r requiremenets.txt
flask run
```

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

## Dockerfile

Dentro de la carpeta raiz del repositorio, construimos la imagen:

```bash
docker build -t test_app:1 .
docker run --rm -dp 5050:5000 test_app:1
curl localhost:5050
```



