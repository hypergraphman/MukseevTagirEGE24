from itertools import permutations
ans = set()
for w in permutations('ВУАЛЬ'):
    word = ''.join(w)
    if word[0] != 'Ь' and 'ЬУ' not in word and 'ЬА' not in word:
        ans.add(word)

print(len(ans))

