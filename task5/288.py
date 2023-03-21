def fun(x):
    s1 = f'{x:b}'
    if x % 2 == 0:
        # s = sum(map(int, s1))
        s = s1.count('1')
        s2 = s1 + f'{s:b}'
    else:
        s2 = '1' + s1 + '00'
    return int(s2, 2)


n = 0
while fun(n) <= 215:
    n += 1
print(n)