a =sorted([80, 30, 50, 40])
users = 0
N = 4
memor = 100
last = None

for j in range(N):
    if memor-a[j] >= 0:
        memor -= a[j]
        users += 1
        last = a[j]
        
memor += last
for j in range(N):
    if memor - a[j] >= 0:
        last = a[j]
print(users, last)
