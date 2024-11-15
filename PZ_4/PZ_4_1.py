#V 24
#1. Даны целые числа A и B (A < B). Вывести все целые числа от A до B включительно при 
# этом число A должно выводиться 1 раз, число A + 1 должно выводиться 2 раза и т.д.

while True:
    try:
        A = int(input("Enter A: "))
        B = int(input("Enter B: "))
        break
    except:
        print("Invalid input. Please enter a number.")

for i in range(A, B+1):
    for j in range(i+1-A):
        print(i)