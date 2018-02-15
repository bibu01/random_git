import requests


url - 'https://dota2.ru/img/heroes/abaddon/m_icon.jpg'

r - requests.get(url, stream=True)

with open('1.jpg', 'bw') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)