"""Посчитать факториал (произведение 1 до N) и
треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов"""

n = int (input ('Введите число: '))
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
 
def triangularNumber(n):
    if n == 1:
        return 1
    return triangularNumber(n - 1) + n

print(f"Факториал числа {n} равняется: {(fac(n))}")
print(f"Треугольное число {n} равняется: {triangularNumber(n)}")

