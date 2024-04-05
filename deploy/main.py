import requests
import json

username = 'jaliagaent'
token = '0aa1753521d2f86b40c8f7c10da1639af269ada0'
domain_name = "jaliagaent.pythonanywhere.com"
with open("app/app.py") as f: app = f.read()
with open("app/static/swagger.json") as f: document = f.read()

#response = requests.get(
#    #'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/static_files/'.format(username=username, domain_name=domain_name),
#    'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/home/{username}/mysite/'.format(username=username),
#    headers={'Authorization': 'Token {token}'.format(token=token)}
#)

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/home/{username}/mysite/flask_app.py'.format(username=username),
    files={"content": app},
    headers={'Authorization': 'Token {token}'.format(token=token)}
)

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/home/{username}/mysite/static/swagger.json'.format(username=username),
    files={"content": document},
    headers={'Authorization': 'Token {token}'.format(token=token)}
)

update = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(username=username, domain_name=domain_name),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)


if response.status_code == 201:
    print("File updated")
    #print(json.loads(response.content.decode("utf-8"))[0]) # 'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/'.format(username=username),
    #print(json.loads(response.content.decode("utf-8")).keys())
#elif response.status_code == 201:
#    print("File updated")

else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
