# Task 1
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'Красный':
            print(self.__color)
            sleep(7)
            self.__color = 'Желтый'
            print(self.__color)
            sleep(2)
            self.__color = 'Зеленый'
            print(self.__color)
            sleep(10)
            print('Finish')
        else:
            print('Error')


a = TrafficLight('Красный')
print(a)
print(type(a))
# print(a.__color)
a.running()
b =TrafficLight('Зеленый')
b.running()


# Task_2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, massa, thick):
        return 'Масса %.1f т.' % (self._width*self._length*massa*thick // 1000)

r = Road(20, 5000)
print(r.calc(25, 5))

# Task 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        print(f'Сотрудник {self.surname} {self.name}.')

    def get_total_income(self):
        total = self._income['wage']+self._income['bonus']
        print(f'Совокупный доход {total}')
    def get_total_income_num(self):
        return self._income['wage']+self._income['bonus']


person = Position('Vladimir', 'Bondarenko', 'student', 25000, 10000)
print(f'Имя сотрудника: {person.name}')
print(f'Фамилия сотрудника: {person.surname}')
print(f'Должность сотрудника: {person.position}')
print(f"Оклад: {person._income['wage']}")
print(f"Премия: {person._income['bonus']}")

person.get_full_name()
person.get_total_income()
total_income = person.get_total_income_num()
print(total_income)


# Task_4

class Car:
    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        pol = 'Обычный'
        if self.is_police:
            pol = 'Полицейский'
        print(pol + ' автомобиль %s поехал !' % self.name)

    def stop(self):
        print('Автомобиль %s остановился !' % self.name)

    def turn(self, direction):
        print('Автомобиль повернул ' + str(direction))

    def show_speed(self):
        print ('Скорость %d км/ч' % (self.speed))

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Скорость %d км/ч. Превышение скорости на %d км/ч' % (self.speed, self.speed - 60))

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print('Скорость %d км/ч. Превышение скорости на %d км/ч' % (self.speed, self.speed - 40))


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

a = Car(50, 'Белый', 'ЛАДА')
a.go()
a.show_speed()
a.turn('налево')
a.turn('направо')
a.stop()

b = TownCar(80, 'Синий', 'ВОЛГА')
b.go()
b.show_speed()
b.stop()

p = PoliceCar(110, 'бело-голубой', 'Alfa Romeo')
p.go()
p.show_speed()
p.stop()

w = WorkCar(55, 'желтый', 'BobCat')
w.go()
w.turn('назад')
w.show_speed()
w.stop()

# Task_5


class Stationary:
    def __init__(self):
        self.title = 'Заготовка'
        print('Класс "Канцелярская принадлежность" успешно создан')
        print('Атрибут '+self.title+' инициализирован !')

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки для РУЧКИ...')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки для КАРАНДАША...')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки для МАРКЕРА...')


a = Stationary()
''' У всех дочерних объектов будет вызван конструктор родителя
о чем при создании дочерних объектов будет выведено сообщение
которое формируется в конструкторе родителя (а значит создан и 
инициализирован атрибут из родительского класса) '''
b = Pen()
c = Pencil()
d = Handle()
a.draw()
b.draw()
c.draw()
d.draw()
