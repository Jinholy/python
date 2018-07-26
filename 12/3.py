a, b = map(int, input().split(' '))
lst = []
result = []
for i in range(a):
    lst.append(i + 1)

idx = 0
while True:
    idx += (b - 1)
    idx = idx % len(lst)
    var = lst[idx]
    result.append(var)
    lst.remove(var)
    if len(lst) == 0:
        break

print("<", ', '.join(map(str, result)), ">", sep='')
