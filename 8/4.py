import math
ipt = input()
ndic = dict()

for i in range(len(ipt)):
    try:
        ndic[int(ipt[i])] += 1
    except:
        ndic[int(ipt[i])] = 1

# a = list(ndic.keys())
sorted_dic = sorted(ndic.items(), key=lambda x: x[1])
# dictionary key로 정렬

# print(ndic)
# print(ndic.popitem())

num_96 = 0
tmp = sorted_dic[:]
for i in tmp:
    if i[0] == 6 or i[0] == 9:
        num_96 += i[1]
        sorted_dic.remove(i)


result = []
result.append(math.ceil(num_96/2)) #반올림이 이상해서안대자낭

if len(sorted_dic) != 0:
    result.append(sorted_dic.pop()[1])
print(sorted(result).pop())
