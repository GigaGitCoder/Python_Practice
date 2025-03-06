# 1. Даны значения роста 20 юношей. Определить, сколько юношей будут направлены в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

import random

def generate_heights():
    heights = []
    for i in range(20):
        heights.append(random.randint(170, 210))
    return heights

def determine_teams(heights):
    basketball_team = []
    football_team = []
    for height in heights:
        if height >= 190:
            basketball_team.append(height)
        else:
            football_team.append(height)
    return basketball_team, football_team

heights = generate_heights()
basketball_team, football_team = determine_teams(heights)
print(f'Рост юношей: {heights}')
print(f'Количество юношей в баскетбольной команде: {len(basketball_team)}')
print(f'Количество юношей в футбольной команде: {len(football_team)}')
