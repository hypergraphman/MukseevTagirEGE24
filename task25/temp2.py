from fnmatch import fnmatch

for i in range(131, 2000000, 131):
    if fnmatch(str(i), '1*53?7') and i % 131 == 0:
        print(i, i // 13)