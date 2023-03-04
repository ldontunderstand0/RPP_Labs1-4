import time

res = ''
time_stamp = time.time()

year = time_stamp / (365 * 24 * 60 * 60)
res += str(int(year) + 1970) + '-'

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = (year - int(year)) * 365 - 12
month = '00'
for i in range(len(months)):
    if days < months[i]:
        month = str(i + 1)
        break
    days -= months[i]
if len(month) < 2:
    month = '0' + month
res += month + '-'

if len(str(int(days))) < 2:
    res += '0' + str(int(days)) + ' '
else:
    res += str(int(days)) + ' '

hours = (days - int(days)) * 24
if len(str(int(hours + 4))) < 2:
    res += '0' + str(int(hours + 4)) + ':'
else:
    res += str(int(hours + 4)) + ':'

minutes = (hours - int(hours)) * 60
if len(str(int(minutes))) < 2:
    res += '0' + str(int(minutes)) + ':'
else:
    res += str(int(minutes)) + ':'

seconds = (minutes - int(minutes)) * 60
if len(str(int(seconds))) < 2:
    res += '0' + str(int(seconds))
else:
    res += str(int(seconds))

print(res)
