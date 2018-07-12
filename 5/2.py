def is_hnum(num):
    result = True
    a = []
    var = str(num)
    length = len(var)

    if length == 1 or length == 2:
        return True

    for i in range(0, length):
        a.append(var[i])

    gap = int(a[1]) - int(a[0])
    for i in range(0, length - 1):
        if int(a[i + 1]) - int(a[i]) != gap:
            result = False
            break

    return result


ipt = int(input())
count = 0
for i in range(1, ipt+1):
    if is_hnum(i):
        count = count + 1

print(count)
