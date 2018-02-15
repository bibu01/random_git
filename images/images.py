import requests


urlt = 'https://dota2.ru/img/heroes/abaddon/m_icon.jpg'

urlt2='axe'

urls = {
    'abaddon',
    'alchemist',
    'axe',
    'beastmaster',
    'brewmaster',
    'bristleback',
    'centaur_warruner',
    'chaos_knight',
    'clockwerk',
    'doom',
    'dragon_knight',
    'earth_spirit',
    'earthshaker',
    'elder_titan',
    'huskar',
    'io',
    'kunkka',
    'legion_commander',
    'lifestealer',
    'lykan',
    'magnus',
    'night_stalker',
    'omniknight',
    'phoenix',
    'pudge',
    'sand_king',
    'slardar',
    'spirit_breaker',
    'sven',
    'tidehunter',
    'timbersaw',
    'tiny',
    'treant_protektor',
    'tusk',
    'underlord',
    'undying',
    'wraithking',
    }


for url in urls:
    s = f'https://dota2.ru/img/heroes/{url}/m_icon.jpg'
    r = requests.get(s, stream=True)
    a = 1
    with open(url+'.jpg', 'bw') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk);
    a= a+1        

    
