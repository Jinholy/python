def get_bag_35(sug):
    result = 0
    while True:
        if sug < 6:
            break
        else:
            sug = sug - 3
            result = result + 1

    return result + sug / 5


def get_bag_53(sug):
    result = 0
    while True:
        if sug < 4:
            break
        else:
            sug = sug - 5
            result = result + 1

    return result + sug / 3


sugar = int(input())

bags = []

bags.append(sugar / 5)
bags.append(sugar / 3)
bags.append(get_bag_35(sugar))
bags.append(get_bag_53(sugar))

result = []
for s in bags:
    if s - int(s) == 0:
        result.append(s)


result.sort()

print(result)

if len(result) == 0:
    print('-1')
else:
    print(int(result[0]))

'''
3+5
6+5
9+5
12+5
15+5
18+5

3+10
3+15
3+20
3+25
'''
'''
var = int(input())

def get_nums(num):
    bag = var // num
    remain = var % num

    if remain == 0:
        result = bag
    elif remain == 3:
        result = bag + 1
    else:
        result = -1

    return result


bag3 = get_nums(3)
bag5 = get_nums(5)

# result = bag5 if bag5>bag3 else bag3 #3항연산 비슷


if bag3 == -1 or bag5 == -1:
    result = bag5 if bag5 > bag3 else bag3
else:
    if bag5 > bag3:
        result = bag3
    else:
        result = bag5

print(result)

'''
