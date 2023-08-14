def divs(n):
    d = []
    for i in range(2,int(n**(0.5)) +1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    return sorted(d)


# def divs(n):
#     d = set()
#     for i in range(2,int(n**(0.5)) +1):
#         if n % i == 0:
#             d.add(i)
#             d.add(n//i)
#     return sorted(d)


for g in range(81234, 134689+1):
    if len(divs(g)) == 3:
        print(g, min(divs(g)), max(divs(g)))