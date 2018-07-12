def func(num):
    tmp = str(num)
    result = 0
    for i in range(0, len(tmp)):
        result = result + int(tmp[i])

    return result + num


self_num = []
all_set = set()
for i in range(0, 10000):
    all_set.add(i)
    if func(i) not in self_num:
        self_num.append(func(i))

result = sorted(all_set - set(self_num))

#print(result, *result, sep='\n')   #왜 이거로 제출하면 오답뜨니

for i in result:
    print(i)