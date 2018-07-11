C = int(input())
v_arr = []
rank = []


def sum_arr(arr):
    result = 0
    for i in range(1, len(arr)):
        result = result + arr[i]

    return result


for i in range(0, C):
    v_arr.append(input())

for arr in v_arr:
    t = list(map(int, arr.split(' ')))
    avg = sum_arr(t) / (len(t)-1)
    cnt = 0
    for i in range(1, len(t)):
        if t[i] > avg:
            cnt = cnt + 1

    rank.append(cnt / (len(t)-1))


for i in rank:
    print('{:.3f}%'.format(i * 100))
