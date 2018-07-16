ipt = input()
list = []
for i in range(0, 26):
    list.append(-1)

for i in range(0, len(ipt)):
    idx = ord(ipt[i]) - 97
    if list[idx] == -1:
        list[idx] = i

print(' '.join(map(str, list)))
