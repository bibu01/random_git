import requests


urls_s = [
    'abaddon',
    'alchemist',
    'axe',
    'beastmaster',
    'brewmaster',
    'bristleback',
    'centaur_warrunner',
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
    'lycan',
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
    'treant_protector',
    'tusk',
    'underlord',
    'undying',
    'wraith_king',
    ]

a = 0
for url in urls_s:
    a= a+1
    s = f'https://dota2.ru/img/heroes/{url}/m_icon.jpg'
    r = requests.get(s, stream=True)
    with open(str(a)+'.jpg', 'bw') as f:
        for chunk in r.iter_content(8192):
            f.write(chunk);

    
