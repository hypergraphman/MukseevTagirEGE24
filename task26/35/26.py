f = open('26.txt')
n = (int(f.readline()))
c = sorted([int(x) for x in f])
k = int(len(c)*0.8)
sbed = sum(c[:k])
sbg = sum(c[k:])
print(sbg*0.8, (sum(c)*0.6-sbg*0.8)/sbed*c[0])



