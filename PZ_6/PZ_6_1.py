#V 24
#1. Дан список ненулевых целых чисел размера N. Проверить, 
# образуют ли его элементы геометрическую прогрессию. Если образуют, 
# то вывести знаменатель прогрессии, если нет — вывести 0.
 
def check_geometric_progression(arr):
    n = len(arr)
    if n < 2:
        return 0  # Нельзя проверить прогрессию, если меньше двух элементов
    # Вычисляем знаменатель прогрессии
    ratio = arr[1] / arr[0]
    
    for i in range(2, n):
        if arr[i] / arr[i - 1] != ratio:
            return False  # Не образуют геометрическую прогрессию
    
    return True

sp = []
for i in range(int(input("Введите длину списка: "))):
    sp.append(int(input(f"Введите {i+1}-й элемент списка: ")))

print(check_geometric_progression(sp))