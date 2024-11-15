#V 24
#2. Даны целые положительные числа N и K. Используя только операции сложения и вычитания,
# найти частное от деления нацело N на K, а также остаток от этого деления.

while True:
    try:
        N = int(input("Enter N: "))
        K = int(input("Enter K: "))
        break
    except:
        print("Invalid input. Please enter a number.")

chast=0
 
while N-K > 0:
    N -= K
    chast += 1

print(f"Частное: {chast}, Остаток: {N}")