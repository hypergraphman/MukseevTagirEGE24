def divs(n):
    d = {1, }
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


array_of_answer = []
for number in range(2, 10001):
    d = divs(number)
    if sum(d) == number:
        print(number, len(d))

