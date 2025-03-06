# 2. Составить список, в который будут включены только согласные буквы и привести их к верхнему регистру. 
# Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир'].

def extract_consonants(cities):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    consonants = []
    for city in cities:
        for char in city:
            if char not in vowels and char.isalpha():
                consonants.append(char.upper())
    return consonants

cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
consonants = extract_consonants(cities)
print(f'Список согласных букв в верхнем регистре: {consonants}')