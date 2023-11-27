def fn(n):
    st = '>'+'1'*23+'2'*n+'3'*25
    while '>1' in st or '>2' in st or '>3' in st:
        if '>1':
            st = st.replace('>1', '1>', 1)
        if '>2':
            st = st.replace('>2', '>3', 1)
        if '>3':
            st = st.replace('>3', '>11', 1)
    return  st

def divs(n):
    chek = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            chek = False
    return chek


for i in range(1000):
    k = [int(x) for x in (fn(i)[:-1])]
    if divs((sum(k))):
        print(i)