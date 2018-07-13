ndic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}

A = int(input())
B = int(input())
C = int(input())


m = A * B * C
var = str(m)
for i in range(0, len(var)):
    ndic[int(var[i])] += 1


for i in range(0,10):
    print(ndic[i])