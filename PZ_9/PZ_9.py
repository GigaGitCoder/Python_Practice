# Задача:
# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', 
# отражающая продажи продукции по дням в кг. 
# Преобразовать информацию из строки в словари, 
# с использованием функции найти минимальные продажи по каждому виду продукции, 
# результаты вывести на экран.

def find_min_sales(data):
    parts = data.split()  # Метод split() разбивает строку на список по пробелам
    sales_dict = {}  
    current_product = None

    for part in parts:
        if part.isalpha():  # Проверяем, является ли часть продуктом (строкой)
            current_product = part  
            sales_dict[current_product] = []  # Инициализируем список для хранения продаж
        else:
            if current_product is not None:  
                sales_dict[current_product].append(int(part))  

    min_sales = {product: min(sales) for product, sales in sales_dict.items()}  # Находим минимальные продажи для каждого продукта
    return min_sales 

data = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'  # Исходная строка с данными о продажах
min_sales = find_min_sales(data) 

for product, min_sale in min_sales.items(): 
    print(f'Минимальные продажи для {product}: {min_sale} кг') 
    