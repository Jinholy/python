arr = [True] * 1000000
arr[0] = False
arr[1] = False


for i in range(len(arr)):
    if arr[i]:
        k = 2
        while True:
            if i * k >= 1000000:
                break
            arr[i * k] = False
            k += 1


def get_prine_cnt(num):
    cnt = 0
    for i in range(num+1, 2 * num+1):
        if arr[i]:
            cnt += 1

    return cnt


lst = []
while True:
    ipt = int(input())
    if ipt == 0:
        break;

    lst.append(get_prine_cnt(ipt))


for i in lst:
    print(i)