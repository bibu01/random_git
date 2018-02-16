import requests


urls_str = [
    'abaddon','alchemist','axe','beastmaster',
    'brewmaster','bristleback','centaur_warrunner',
    'chaos_knight','clockwerk','doom','dragon_knight',
    'earth_spirit','earthshaker','elder_titan','huskar',
    'io','kunkka','legion_commander','lifestealer',
    'lycan','magnus','night_stalker','omniknight',
    'phoenix','pudge','sand_king','slardar',
    'spirit_breaker','sven','tidehunter','timbersaw',
    'tiny','treant_protector','tusk','underlord',
    'undying','wraith_king'
    ]

urls_agl = [
    'anti_mage','arc_warden','bloodseeker','bounty_hunter',
    'broodmother','clinkz','drow_ranger','ember_spirit',
    'faceless_void','gyrocopter','juggernaut','lone_druid',
    'luna','medusa','meepo','mirana',
    'monkey_king','morphling','naga_siren','nyx_assassin',
    'pangolier','phantom_assassin','phantom_lancer','razor',
    'riki','shadow_fiend','slark','sniper',
    'spectre','templar_assassin','terrorblade','troll_warlord',
    'ursa','vengeful_spirit','venomancer','viper',
    'weaver'
    ]

urls_int = [
    'ancient_apparition','bane','batrider','chen',
    'crystal_maiden','dark_seer','dark_willow','dazzle',
    'death_prophet','disruptor','enchantress','enigma',
    'invoker','jakiro','keeper_of_the_light','leshrac',
    'lich','lina','lion','natures_prophet',
    'necrophos','ogre_magi','oracle','outworld_devourer',
    'puck','pugna','queen_of_pain','rubick',
    'shadow_demon','shadow_shaman','silencer','skywrath_mage',
    'storm_spirit','techies','tinker','visage',
    'warlock','windranger','winter_wyvern','witch_doctor',
    'zeus'
    ]


def parcing(a,urls):
    for url in urls:
        a = a + 1
        s = f'https://dota2.ru/img/heroes/{url}/m_icon.jpg'
        r = requests.get(s, stream=True)
        with open(str(a)+'.jpg', 'bw') as f:
            for chunk in r.iter_content(8192):
                f.write(chunk);
    return a
    
a = 0
print('hello')
a = parcing(a,urls_str)
a = parcing(a,urls_agl)
a = parcing(a,urls_int)
    
