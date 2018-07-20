arr = [True] * 10000
arr[0] = False
arr[1] = False

for i in range(len(arr)):
    if arr[i]:
        k = 2
        while True:
            if i * k >= 10000:
                break
            arr[i * k] = False
            k += 1

prime_arr = []
for i in range(0, len(arr)):
    if arr[i]:
        prime_arr.append(int(i))


def get_goldbach_num(num):
    goldbach_lst = []
    for i in range(0, len(prime_arr)):
        k = prime_arr[i]
        for j in range(0, len(prime_arr)):
            m = prime_arr[j]
            if k + m == num:
                goldbach_lst.append([k, m])

    goldbach_lst.sort(key=lambda x: abs(x[1] - x[0]))
    return goldbach_lst[0]


#    return result


ipt = int(input())
lst = []
for i in range(ipt):
    lst.append(int(input()))

for i in lst:
    print(' '.join(map(str, get_goldbach_num(i))))
