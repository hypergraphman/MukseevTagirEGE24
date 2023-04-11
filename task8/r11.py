from itertools import product

words = product('ШКОЛА', repeat=3)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('К') == 1:
        k += 1
print(k)