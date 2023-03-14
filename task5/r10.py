def f(x):
    a = x%2
    b = x%3
    c = x%5
    st = (str(a)+str(b)+str(c))
    return st
t = []
for i in range(10, 100):
    if (int(f(i)) == 104):
        t.append(i)

print(min(t))

