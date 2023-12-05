def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a = []
z = 40
for z in range(40, 100):
    for x in range(z, 39, -1):
        y = z - x
        if is_prime(4 * x + 3 * y):
            a.append((x + 2 * y, x, y, z, 4 * x + 3 * y))
print(a)