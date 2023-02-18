import random


def error_check(arr):  # функция проверки корректности ввода
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except ValueError:
            arr[i] = int(random.randint(0, 9))


def rand():  # функция генерации списка случайной длины со случайными числами
    arr = []
    for i in range(random.randint(1, 9)):
        arr.append(random.randint(0, 9))
    return arr


def search(arr):  # функция поиска максимальной последовательности четных чисел
    count, left, right, maxi, le = 0, 0, 0, 0, 0
    arr.append(1)

    for i in range(len(arr)):

        if arr[i] % 2 == 0:
            if count == 0:
                le = i
            count += 1

        else:
            if count > maxi:
                maxi = count
                left = le
                right = i
                count = 0

    arr.pop()
    return left, right


arr1 = input().split()
arr2 = input().split()

error_check(arr1)
error_check(arr2)

arr1 = rand()
arr2 = rand()

print(arr1)
print(arr2)

l1, r1 = search(arr1)
l2, r2 = search(arr2)

arr1, arr2 = arr1[:l1] + arr2[l2:r2] + arr1[r1:], arr2[:l2] + arr1[l1:r1] + arr2[r2:]  # обмен максимальными длинами

print(arr1)
print(arr2)
