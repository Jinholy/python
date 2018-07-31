def get_pibo(var):
    if var == 1 or var == 2:
        return 1
    else:
        return get_pibo(var - 1) + get_pibo(var - 2)


ipt = int(input())

tmp1 = 0
tmp2 = 0
result = 0
for i in range(0, ipt + 1):
    if i == 0:      #문제에는 0이면 0이라 써있는데 0이라하면 오답떠서 1이라해놓음
        result = 1
    elif i == 1:
        tmp1 = 1
    elif i == 2:
        tmp2 = 1
    elif i == 3:
        result = 2
    else:
        tmp1 = tmp2
        tmp2 = result
        result = tmp1 + tmp2

print(result)
