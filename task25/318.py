a = []
for i in range(1000001268, 2 * 10 ** 9, 2023):
    t = str(i)
    if t[0] == t[-1] == '1':
        a.append(t)
for i in a:
    if sum(map(int, i)) == 68:
        print(i, int(i) // 2023)