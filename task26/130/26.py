f = open('26-130.txt')
n = int(f.readline())
count = [0] * 24 * 60
for _ in range(n):
    s, e = map(int, f.readline().split())
    for i in range(s, e + 1):
        count[i] += 1

max_value = max(count)

k = 0
for i in range(1, len(count)):
    if count[i] == max_value and count[i] > count[i - 1]:
        k += 1
print(k)
print(max_value)