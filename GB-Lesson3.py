# Task 1
def func1(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('Error! Division by zero !!!')
        return None

a = float(input('Enter first parameter: '))
b = float(input('Enter second parameter: '))
print(func1(a, b))

# Task 2
def func2 (f_name, s_name, b_date, city, e_mail, phone):
    return f_name + ' ' +s_name + ', was born ' + str(b_date) + ' in '+city +'. Contact: '+ phone + ', '+e_mail+'.'

print(func2(f_name='Vladimir', s_name = 'Bondarenko', b_date=2000, city = 'Samara', phone ='+7(123)456-78-90', e_mail='bond@mail.ru'))

# Task 3
def func_max(a, b, c):
    m1 = a
    m2 = b
    if b > m1:
        m1 = b
        m2 = a
    if c > m1:
        m2 = m1
        m1 = c
    elif c > m2:
        m2=c
    print(f'{m1}  {m2}')
    return m1+m2

print(func_max(2, 1, 3))

# Task 4
def my_func1(x, y):
    res = x ** abs(y)
    return 1 / res
def my_func2(x, y):
    res = 1
    for i in range(abs(y)):
        res = res * x
    return 1 / res
print (my_func1(2.9, -16))
print (my_func2(2.9, -16))

# Task 5
global flag
flag = False
my_sum = 0
def sum_str(s):
    str_list = s.split()
    sum = 0
    global flag
    try:
        for i in range(len(str_list)):
            a = float(str_list[i])
            if abs(a) < 0.00001:
                flag = True
                return sum
            sum = sum + a
    except:
        print('Errors in data !!!')
        return None
    return sum

while not flag:
    ss = input('Enter numbers: ')
    my_sum = my_sum + sum_str(ss)
    print (my_sum)




# Task 6, 7
def int_func (s):
    #s = str(s)
    a = s[0]
    a = a.upper()
    s = a + s[1:]
    return s
print (int_func('testext'))

str = input ('Enter string: ')
str_list = str.split()
print (str_list)

new_str = ''
for i in range(len(str_list)):
    new_str = new_str+ ' ' +int_func(str_list[i])
new_str = new_str[1:]

print (new_str)



