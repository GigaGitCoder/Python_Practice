# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in range(1, matrix.shape[0], 2):
    average = np.mean(matrix[i])
    print(f"Среднее арифметическое строки {i + 1}: {average}") 