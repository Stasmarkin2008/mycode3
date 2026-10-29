import json
import urllib.request
username=input()
url=f'https://api.github.com/users/{username}'
with urllib.request.urlopen(url) as f:
    d = json.loads(f.read().decode('utf-8'))
    name=d.get('login')
    repoz=d.get('public_repos')
    urll=d.get('html_url')
    folov=d.get('followers')
print(f'Имя {name}')
print(f'Количество публичных репозиториев {repoz}')
print(f'Cылка на страницу {urll}')
print(f'Количество подписчиков {folov}')
