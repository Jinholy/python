import sys

ipt = int(input())
list = []

for i in range(0, ipt):
     list.append(input())

for i in range(0, ipt):
    A, B = list[i].split(' ')
    for j in range(len(B)):
        sys.stdout.write(B[j] * int(A))
    print()
