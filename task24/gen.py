from string import ascii_uppercase, digits
from random import choice

f = open('24.txt', 'w')
alf = ascii_uppercase + digits
for _ in range(10_000_000):
    f.write(choice(alf))