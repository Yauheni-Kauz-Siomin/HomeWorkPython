""" Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no"""

n = int (input ('Введите количество долек шоколадки по ширине: '))
m = int (input ('Введите количество долек шоколадки по длине: '))
k = int (input ('Введите количество долек, которые необходимо отломить: '))
if k < m * n and (k % n == 0 or k % m == 0):
    print("Шоколадку получиться разломить на два прямоугольника!")
else:
    print("Разломить шоколадку на два прямоугольника НЕ получиться сделать!")