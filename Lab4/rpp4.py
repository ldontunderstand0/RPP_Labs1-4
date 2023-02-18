import os

p = 'C:/Users/airja/PycharmProjects/project1'
print('Файлов в папке ' + p + ': ' + str(len(os.listdir(p))))


class Row:
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val


class Model(Row):

    idx, post_num, com_num, date, text, likes = 0, 0, 0, '', '', 0

    def __init__(self, idx: int, post_num: int, com_num: int, date: str, text: str, likes: int):
        super().__init__(idx)
        self.idx = idx
        self.post_num = post_num
        self.com_num = com_num
        self.date = date
        self.text = text
        self.likes = likes

    def __str__(self):
        return f'id: {self.idx}, номер поста: {self.post_num}, номер комментария: {self.com_num}, ' \
               f'дата: {self.date}, текст: {self.text}, кол-во лайков: {self.likes}'

    def __repr__(self):
        return f'model(idx={self.idx},post_num={self.post_num},com_num={self.com_num},' \
               f'date={self.date},text={self.text},likes={self.likes})'

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value


class Data:

    file_path = ''
    data = {}
    pointer = 0

    def __init__(self, file):
        self.file_path = file
        self.data = self.parse(file)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f'Контейнер хранит в себе следущее:\n{d_str}'

    def __repr__(self):
        return f'Data({[repr(rm) for rm in self.data]})'

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer - 1]

    def __getitem__(self, ite):
        if not isinstance(ite, int):
            raise TypeError('Индекс должен быть целым числом')
        if 0 <= ite < len(self.data):
            return self.data[ite]
        else:
            raise IndexError('Неверный индекс')

    def as_generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    @staticmethod
    def parse(file):
        parsed = []
        with open(file, "r") as raw_csv:
            for line in raw_csv:
                (idx, post_num, com_num, date, text, likes) = line.replace("\n", "").split(";")
                parsed.append(Model(int(idx), int(post_num), com_num, date, text, likes))
        return parsed

    def sorted_by_str(self):
        return sorted(self.data, key=lambda f: f.text)

    def sorted_by_number(self):
        return sorted(self.data, key=lambda f: f.post_num)

    def value(self, value):
        r = []
        for d in self.data:
            if d.post_num > value:
                r.append(d)
        return r

    def add_new(self, post_num, com_num, date, text, likes):
        self.data.append(Model(len(self.data) + 1, post_num, com_num, date, text, likes))
        self.save(self.file_path, self.data)

    @staticmethod
    def save(file, new_data):
        with open(file, "w", encoding='utf-8') as f:
            for r in new_data:
                f.write(f"{r.idx},{r.post_num},{r.com_num},{r.date},{r.text},{r.likes}\n")

    def print(self):
        for r in self.data:
            print(f'id: {r.idx}, номер поста: {r.post_num}, номер комментария: {r.com_num}, '
                  f'дата: {r.date}, текст: {r.text}, кол-во лайков: {r.likes}')

    @staticmethod
    def print_d(d):
        for r in d:
            print(f'id: {r.idx}, номер поста: {r.post_num}, номер комментария: {r.com_num}, '
                  f'дата: {r.date}, текст: {r.text}, кол-во лайков: {r.likes}')


data = Data("data.csv")

# __repr__()
print(repr(data), "\n")

# __str__()
print(data, "\n")

# Итератор
for item in iter(data):
    print(item)
print('')
# Генератор
for item in data.as_generator():
    print(item)
print('')
data.print_d(data.sorted_by_number())  # сортировка по номеру
print('')
data.print_d(data.sorted_by_str())  # сортировка по имени
print('')
data.print_d(data.value(3))  # номер больше 3
