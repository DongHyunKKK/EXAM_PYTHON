# 12.4
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])

# 12.5
string = input('문자열 여러개 입력 하세요 : ').split()
numbers = input('숫자 여러개 입력 하세요 : ').split()
result = dict(zip(string, numbers))
print(result)