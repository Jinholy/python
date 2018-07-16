A, B = input().split(' ')

lst = []
lst.append(A[::-1])
lst.append(B[::-1])

lst.sort()

print(lst[1])
