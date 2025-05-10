# В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя 
# (например, 1821 года, 1837 год, 1843 году и так далее  по всему тексту). 
# Посчитать количество полученных элементов.
import re


with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'\b(18[2-8][0-9])(?:\s*[-–]\s*(18[2-8][0-9]))?\s*(?:год[ауе]?|гг?\.|годах?|году)?\b'

matches = re.findall(pattern, text)

print(f"Всего найдено {len(matches)} упоминаний годов:")
for year in sorted(set(matches)): 
    print(f"- {year} год")

print(f"\nОбщее количество упоминаний: {len(matches)}")
