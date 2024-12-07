# задача № 1
with open('tp1.txt', 'w', encoding='utf-8') as f:
    line = ' '
    while line != ' ':
        line = input()
        print(line, file=f)

# задача №2
with open('tp2.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for i, line in enumerate(text, 1):
        words = len(line.split())
        print(f'{i}  строка содержит {words} cлов')

# задача №3

with open('tp3.txt', 'r', encoding='utf-8') as f:
    sal = []
    poor = []

    for i in f:
        i = i.split()
        if float(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')

# задача №4
dic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('tp4.txt', 'r') as file_obj:

    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(dic[i[0]] + '  ' + i[1])
    print(new_file)

with open('tp4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# задача №5
from random import randint
with open('tp5.txt', 'w') as f:
    li = [randint(1, 20) for _ in range(50)]
    f.write(' '.join(map(str, li)))
print('Сумма чисел: ', sum(li))

# задача №6
with open('tp6.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        new = ' '
        for el in line:
            new = ' '.join([new, (el if el in '1234567890' else ' ')])
        res = [int(i) for i in new.split()]
    print(f'{line.split()[0]} - {sum(res)} часов занятий')

# задача №7

import json
with open('tp7j.json', 'w+', encoding='utf-8') as f_write:
    with open('tp7.txt', 'r', encoding='utf-8') as f_read:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_read for line in f_read}
        res = sum([int(i) for i in profit.values() if int(i) > 0]), len([int(i) for i in profit.values() if int(i) > 0])
    doc = [profit, {'average_profit': res}]
    json.dump(profit, f_write)





