len = int(input())
ipt = list(map(int, input().split(' ')))

cnt = 1
for i in range(len):
    print(ipt[i-1], ipt[0] + i-1)
    if ipt[i-1] == (ipt[0] + i-1):
        cnt += 1


print(cnt)