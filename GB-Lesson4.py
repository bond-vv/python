# Task 1
from sys import argv
name, h, stavka, p = argv
salary = float(h) * float(stavka) + float(p)
print(f'Script name = {name}')
print(f'Salary is {salary}')

# Task 2
ls1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(ls1)
ls2 = [i for i in ls1 if ls1.index(i) > 1 and i > ls1[ls1.index(i)-1]]
print(ls2)

# Task 3
# я сделал для отрезка, т.к. из задания непонятно, что такое "в пределах"
# для интервала нужно заменить на range(11, 240)
bb = [i for i in range(10, 241) if i % 20 == 0 or i % 21 == 0]
print(bb)

# Task 4
q = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
q1 = [i for i in q if q.count(i) == 1]
print(q1)

# Task 5
w = [i for i in range(10, 1001) if i % 2 == 0]
print(w)
from functools import reduce
w0 = reduce(lambda a, b: a * b, w)
print(w0)

# Task 6
from itertools import count
start = int(input('Enter first number: '))
for i in count(start):
    if i <= 20:
        print(i)
    else:
        break

lst = [100, 200, 300, 400]
from itertools import cycle
cnt = 0
ln = len(lst)
for j in cycle(lst):
    if cnt < 3 * ln:
        print(j)
        cnt += 1
    else:
        break


# Task 7
def fact(n):
    ff = 1
    for i in range(1, n+1):
        ff *= i
        yield ff


for x in fact(10):
    print(x)
