import sys
'''

N, X = map(int, input().split(' '))

a = list(map(int, input().split(' ')))
a.sort()
idx = a.index(X)

for i in range(0, idx):
    print(a[i])

#입력받은 순서대로 하래 ㅋㅋㅋㅋㅋ
'''

N, X = map(int, input().split(' '))

a = map(int, input().split(' '))
b = []

for i in a:
    if i < X:
        b.append(i)
    else:
        pass


for i in b:
    print(i, end=" ")

