dic = dict()

for i in range(ord('a'), ord('s')):
    dic[chr(i)] = (i - 97) // 3 + 3

dic['s'] = 8


for i in range(ord('t'), ord('z') + 1):
    dic[chr(i)] = (i - 116) // 3 + 9

dic['z'] = 10


ipt = input().lower()
result = 0

for i in range(len(ipt)):
    result += dic[ipt[i]]

print(result)
