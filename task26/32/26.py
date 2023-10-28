from math import *

f = open('26-s1.txt')
n = int(f.readline())
a = sorted([int(x) for x in f])
find_i = None
for i in range(len(a)):
    if a[i] > 150 and not find_i:
        find_i = i
        break
b = a[find_i:]
s = sum(a[:find_i]) + ceil(sum(b[:len(b) // 2]) * 0.8) + sum(b[len(b) // 2:])
print(s, b[len(b) // 2 - 1])
