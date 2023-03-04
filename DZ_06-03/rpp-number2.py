t = [int(input()) for y in range(0, int(input()))]
mini = t[0]

for i in t:
    if i < mini:
        mini = i

print(mini)
