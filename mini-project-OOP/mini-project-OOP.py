class Math:

    # глобальная переменная
    id = 0

    # конструктор
    def __init__(self):
        Math.id += 1

    # определение метода str
    def __str__(self):
        return 'Math class Object'

    @staticmethod
    # полиморфизм : переопределение метода
    def info():
        return 'Math is math'


# наследование
class Operation(Math):

    # конструктор
    def __init__(self, value):
        super().__init__()
        self.value = value

    # свойство
    @property
    def value(self):
        # модификатор доступа
        return self.__value

    # cеттер
    @value.setter
    def value(self, value):
        if value > 5:
            self.__value = 5
        elif value < 1:
            self.__value = 1
        else:
            self.__value = value

    # определение метода str
    def __str__(self):
        return 'Operation class Object'

    # полиморфизм : переопределение метода
    def info(self):
        return 'Operation is math change of object'


# множественное наследование
class Sum(Operation):

    # определение метода str
    def __str__(self):
        return 'Sum class Object'

    @staticmethod
    # полиморфизм : перегрузка
    # модификатор доступа
    def sum(_a, _b, _c=None):
        if _c is None:
            return 'a + b = ' + str(_a + _b)
        else:
            return 'a + b + c = ' + str(_a + _b + _c)

    # полиморфизм : переопределение метода
    def info(self):
        return 'Sum is operation of addition'


# множественное наследование
class Mult(Operation):

    # определение метода str
    def __str__(self):
        return 'Mult class Object'

    @staticmethod
    # полиморфизм : перегрузка
    # модификатор доступа
    def mult(_a, _b, _c=None):
        if _c is None:
            return 'a * b = ' + str(_a * _b)
        else:
            return 'a * b * c = ' + str(_a * _b * _c)

    # полиморфизм : переопределение метода
    def info(self):
        return 'Mult is operation of multiplication'


a = 5
b = 6
c = 7
val = 3
m = Mult(val)
print(m)
print('id = ' + str(m.id))
print(m.mult(a, b))
print(m.mult(a, b, c))
print(m.info())
print('Value = ' + str(m.value))
