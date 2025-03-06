# 1. В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива
import numpy as np

matrix = np.array([[1, -2, 3], [-4, 5, -6], [7, 8, -9]])
negative_elements = []
for row in matrix:
    for element in row:
        if element < 0:
            negative_elements.append(element)
print(len(negative_elements)) 