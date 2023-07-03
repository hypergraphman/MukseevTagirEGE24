s = open('24-264.txt').read()
mx = 1
len = 1
for p1, p2 in zip(s, s[1:]):
    if p1.isalpha() != p2.isalpha():
        len += 1
        if len > mx:
            mx = len
    else:
        len = 1
print(mx)