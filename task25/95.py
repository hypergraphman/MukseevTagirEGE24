s = 0
for n in range(1395, 22718):
    check = True
    number = str(n)

    for i in range(1, len(number)):
        if number[i - 1] > number[i]:
            check = False

    if check:
        s += n

print(s)


