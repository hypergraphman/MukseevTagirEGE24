s = 0

for n in range(2945, 18294 + 1):
    check = True
    for dels in range(2, int(n ** 0.5) + 1):
        if n % (dels * dels) == 0:
            check = False
            break
    if check:
        for digit in str(n):
            s += int(digit)

print(s)