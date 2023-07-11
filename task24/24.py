s = open('24.txt').read()

# задача 1
count = 0
for i in range(len(s) - 2):
    c1, c2, c3 = s[i], s[i + 1], s[i + 2]
# for c1, c2, c3 in zip(s, s[1:], s[2:]):
    if c1 in 'BCD' and c2 in 'BDE' and c1 != c2 and c3 in 'BCE' and c2 != c3:
        count += 1
print(count)

# задача 2
length = 1
max_len = 1
for i in range(len(s) - 1):
    c1, c2 = s[i], s[i + 1]
    if c1 > c2:
        length += 1
        if length > max_len:
            max_len = length
    else:
        length = 1
print(max_len)

# Задача 3
is_num = False
left_i = None
mx = 0
for i, c in enumerate(s):
    if c.isdigit() and not is_num:
        left_i = i
        is_num = True
    if not c.isdigit() and is_num and s[i - 1] in '13579':
        mx = max(mx, int(s[left_i: i]))
        is_num = False
print(mx)
