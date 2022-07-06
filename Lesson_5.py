# Task 1
with open('task1.txt', 'w') as file:
    s = str(input('Enter string. (Press ENTER to stop):'))
    while s != '':
        file.write(s+'\n')
        s = str(input('Enter string. Press ENTEr to exit^'))
print('===== TASK 2 =====================================')

# Task 2
with open('task2.txt', 'r') as file2:
    lines = 0
    for i in file2:
        lines += 1
 #       words = 0
 #       s = file2.readline()
        words = len(i.split())
        print(f'Строка {lines} содержит {words} слов.')
    print(f'Всего строк в файле: {lines}.')

print('========= TASK 3 =================================')
# Task 3

with open('task3.txt', 'r') as file3:
#    d = {}
    par = 20000.0
    print(f'Струдники с окладом менее {par:.2f}:')
    summ = 0
    cnt = 0
    for line in file3:
 #       d[str(line.split()[0])] = float(line.split()[1])
        cnt += 1
        a = str(line.split()[0])
        b = float(line.split()[1])
        summ += b
        if b < par:
            print(f'{a} имеет доход {b:.2f}.')
print(f'Средняя зарплата: {(summ / cnt):.2f}')
print('================ TASK 4 ==========================')

# Task 4
d = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('task4.txt', 'r') as file4_in:
    with open('task4_out.txt', 'w') as file4_out:
        for line in file4_in:
            file4_out.write(d[int(line.split()[2])]+' '+' '.join(line.split()[1:])+'\n')
print('=================== TASK 5 ==========================')

# Task 5

from random import randint as rnd
n = 10
with open('task5.txt', 'w') as file5:
    for i in range(5):
        for j in range(n):
            file5.write(str(rnd(1, 100))+' ')
        file5.write('\n')

from functools import reduce as rd
with open('task5.txt', 'r') as file5:
    summ = 0
    for ln in file5:
        summ = rd(lambda x,y: x+int(y), ln.split(), summ)
print('Сумма элементов файла равна ', summ)

print('=================== TASK 6 ==========================')

# Task 6
with open('task6.txt', 'r') as file6:
    res = {}
    for ln in file6:
        s = ln.split()
        r = 0
        for el in s[1:]:
            if el.find('-') >= 0:
                a = 0
            elif el.find('(') >= 0:
                a = int(el[:el.find('(')])
            r +=a
        print(s)
        res[s[0][:-1]] = r
    print(res)

print('=================== TASK 7 ==========================')

# Task 7

with open('task7.txt', 'r') as file7:
    firms = {}
    avg_profit = 0
    n = 0
    for ln in file7:
        slist = ln.split()
        if slist[2].isdigit() and slist[3].isdigit():
            a = float(slist[2]) - float(slist[3])
            firms[slist[0]] = a
            if a > 0:
                avg_profit += a
                n += 1
    if n != 0:
        avg_profit /= n
    print(avg_profit)
    firms_report = [firms, {'average_profit': avg_profit}]
    print(firms_report)
import json
with open('task7.json', 'w') as json_file:
    json.dump(firms_report, json_file)