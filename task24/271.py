def is_check(n):
    num = s[n + 1: n + 7]
    try:
        r = int(num[:2], 16)
        g = int(num[2:4], 16)
        b = int(num[4:], 16)
        return b < r > g
    except:
        pass
    return False


s = open('24-271.txt').read()

amount = 0
for i in range(len(s)):
    if s[i] == '#':
        amount += is_check(i)
print(amount)