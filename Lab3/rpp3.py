import os.path


def print_dict(d):
    print('')
    for k, v in d.items():
        print(str(k) + '\t' + str(v['post_num']) + '\t' + str(v['com_num'])
              + '\t' + v['date'] + '\t' + v['text'] + '\t' + str(v['likes']))


def sort1(d, name):
    return dict(sorted(d.items(), key=lambda f: f[1][name]))


def sort2(d, name, val):
    return dict((k, v) for k, v in d.items() if v[name] > val)


def add(f, d, post_num, com_num, date, text, likes):

    for k, v in d.items():
        f.write(f"{k};{v['post_num']};{v['com_num']};{v['date']};{v['text']};{v['likes']}\n")
    f.write(f"{len(d) + 1};{post_num};{com_num};{date};{text};{likes}\n")

    d.update({len(d) + 1: {'post_num': post_num, 'com_num': com_num,
                           'date': date, 'text': text, 'likes': likes}})


p = 'C:/Users/airja/PycharmProjects/project1'
file_count = 0
print('Файлов в папке ' + p + ': ' + str(len(os.listdir(p))))

file = open("data.csv", "r")
di = {}
for i in file:
    i = i.split(';')
    di.update({int(i[0]): {'post_num': int(i[1]), 'com_num': int(i[2]),
                           'date': i[3], 'text': i[4], 'likes': int(i[5])}})
file.close()

print_dict(di)
print_dict(sort1(di, 'date'))  # сортировка по дате
print_dict(sort1(di, 'likes'))  # сотрировка по лайкам
print_dict(sort2(di, 'post_num', 3))  # сотрировка по критерию

file = open("data.csv", "w")
add(file, di, 4, 2, '04.02.2023 19:00', 'это комментарий', 11)
file.close()
