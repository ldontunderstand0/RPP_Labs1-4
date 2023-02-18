import numpy
import random

n = random.randint(3, 6)
m = random.randint(3, 6)
k = random.randint(1, m)
a = numpy.random.randint(0, 9, (n, m))

input_file = open("input.txt", "w")
input_file.write('n = ' + str(n) + ' m = ' + str(m) + ' k = ' + str(k) + '\n' + str(a))
input_file.close()

for i in range(n):
    f = a[i][k - 1]
    for j in range(m):
        a[i][j] *= f

output_file = open("output.txt", "w")
output_file.write(str(a))
output_file.close()
