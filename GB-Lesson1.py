# Task 1
pass_ok = "777"
pass_entered = input("Enter password ")
access = False
if pass_entered != pass_ok:
    print("Access Denied !!!")
else:
    print('Access Granted !!!')
    access = True
print(access)
n = int(input('Enter integer: '))
while n <= 10:
    print(n)
    n += 1
print('The End !')



# Task 2
n = int(input('Enter seconds: '))
h = n // 3600
n = n % 3600
m = n // 60
s = n % 60
print('Time is:    %d:%02d:%02d' % (h, m, s))

# Task 3
n = int(input('enter digit: '))
nn = 10 * n + n
nnn = 100 * n + nn
res = n + nn + nnn
print('Sum is %d' % res)

# Task 4
n = int(input('Enter positive number: '))
while n <= 0:
    print('Error! Negative integer !')
    n = int(input('Enter positive number: '))
max = 0
while n > 0:
    m = n % 10
    if m > max:
        max = m
    n = n / 10
print('Max digit is %d' % max)


# Tasks 5, 6
incom = float(input('Enter firm\'s income: '))
cost = float(input('Enter firm\'s costs: '))
profit = incom - cost
if profit > 0:
    print('Firm got profit !')
else:
    print('Firm got loss !')
if profit > 0:
    rank = profit / incom
    print('Firm got rank = %.3f' % rank)
    empl = int(input('Enter num of emploeers: '))
    prof_per_empl = profit / empl
    print('Profite per emploeer %.4f' % prof_per_empl)


# Task 7
a = int(input('Enter first day distance: '))
b = int(input('Enter goal distance: '))
while a>b:
    print('Your entered wrong data. Should be a<b')
    a = int(input('Enter first day distance: '))
    b = int(input('Enter goal distance: '))
i = 1
while a < b:
    print('Day %d: km: %.2f' % (i, a))
    a = a * 1.1
    i = i + 1
print('Day %d: km: %.2f' % (i, a))
print('Need %d day(s)' % i)
