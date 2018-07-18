ipt = input()

lst = []

for i in range(len(ipt)):
    lst.append(int(ipt[i]))

lst = sorted(lst, reverse=True)

print(''.join(map(str, lst)))
