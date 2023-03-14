def f(x):
    x = str(x)
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    g = int(x[3])
    mas = [a+b, b+c, c+g]
    mas.remove(min(mas))
    mas.sort()
    return int(str(mas[0]) + str(mas[1]))


t = []
for i in range(1000, 10000):
    if f(i) == 511:
        t.append(i)

print(min(t), max(t))


