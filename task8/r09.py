from itertools import permutations
words = permutations('ВУАЛЬ')
ans = set()
for w in words:
    word = ''.join(w)
    if word[0] != 'Ь' and 'ЬУ' not in word and 'ЬА' not in word:
        ans.add(word)

print(len(ans))

