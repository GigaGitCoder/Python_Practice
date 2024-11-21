#V 24
#3. Дано множество A из N точек (точки заданы своими координатами x, у). 
# Найти пару различных точек этого множества с максимальным расстоянием 
# между ними и само это расстояние (точки выводятся в том же порядке, в 
# котором они перечислены при задании множества A). 
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: 
# R = √(x2 – x1)2 + (у2 – y1)2 . 
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый 
# список для хранения абсцисс, второй — для хранения ординат.

abciss = []
ordinate = []
max_distance = 0
max_pair = []

for i in range(int(input("Введите количество точек: "))):
    abciss.append(int(input(f"Введите {i+1}-ю абсциссу: ")))
    ordinate.append(int(input(f"Введите {i+1}-ю ординату: ")))

max_pair = [None, None]
max_distance = 0

for i in range(len(abciss)):
    for j in range(i + 1, len(abciss)):
        # Вычисление расстояния между точками i и j
        distance = ((abciss[j] - abciss[i]) ** 2 + (ordinate[j] - ordinate[i]) ** 2) ** 0.5
        
        # Если текущее расстояние больше максимального, обновляем максимальное расстояние и пару
        if distance > max_distance:
            max_distance = distance
            max_pair = (i, j)

# Вывод результата
if max_pair[0] is not None and max_pair[1] is not None:
    print(f"Максимальное расстояние: {max_distance}")
    print(f"Пара точек с максимальным расстоянием: ({abciss[max_pair[0]]}, {ordinate[max_pair[0]]}), ({abciss[max_pair[1]]}, {ordinate[max_pair[1]]})")
else:
    print("Нет доступных точек для вычисления расстояния.")
    