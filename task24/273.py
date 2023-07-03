s = open('24-263.txt').read()
mx = 1
len = 1
for p1, p2 in zip(s, s[1:]):
    if p1 != p2:
        len += 1
        if len > mx:
            mx = len
    else:
        len = 1
print(mx)