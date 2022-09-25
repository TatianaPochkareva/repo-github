# задача №1
from sys import argv
def sal():
    try:
        hours, rate, bonus = map(float, argv[1:])
        print('заработная плата сотрудника: ', hours * rate + bonus)
    except ValueError:
        print("Введите данные: часы, ставка, премия")

# задача №2
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_li = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
print(new_li)

# задача №3
li = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(li)

# задача № 4
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_li = [i for i in li if li.count(i) == 1]
print(new_li)

# задача №5
from functools import reduce
li = [i for i in range(100, 1001) if i % 2 == 0]
res = reduce(lambda a, b: a * b, li)

# задача № 6
from itertools import count
st = int(input('Введите стартовое целое число '))
end = int(input('Введите конечное целое число '))
for i in count(st):
    print(i)
    if i == end:
        break



from itertools import cycle
li = [True, 'hello', 398, 43.87, 55, ]
for i in cycle(li):
    end = input('Для окончания цикла введите "стоп"')
    if end.lower() == 'стоп':
        break
    print(i)

# задача №7
def fact(a):
    res = 1
    if a == 0:
        yield f'{a}! = 1'
    for i in range(1, a + 1):
        res *= i
        yield f'{i}! = {res}'

n = int(input('введите число: '))
for el in fact(n):
    print(el)


