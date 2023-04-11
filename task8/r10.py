from itertools import permutations

words = permutations('КАПКАН')
s = set()
for w in words:
    word = ''.join(w)
    if 'КК' not in word and 'АА' not in word:
        s.add(word)

print(len(s))