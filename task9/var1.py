a = open('9.csv')
k = 0
for n in a:
    s = sorted(map(int, n.split(';')))
    if 2 * s[-1] < sum(s[:-1]) and s[0] + s[3] == s[2] + s[1]:
            k += 1
print(k)

a = open('9.csv')
res = list(filter(lambda s: 2 * s[-1] < sum(s[:-1]) and s[0] + s[3] == s[2] + s[1], [sorted(map(int, n.split(';'))) for n in a]))
print(len(res))
