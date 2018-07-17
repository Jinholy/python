ipt = int(input())

cnt = 0
i = 0
bcnt = 0
while True:
    bcnt = cnt
    cnt += i
    if cnt >= ipt:
        break

    i += 1

# i가 홀수면 분자 감소 분모증가
# 짝수면 분자감소 분모증가
if i % 2 != 0:
    bz = (i + 1) - (ipt - bcnt)
    bm = i - bz + 1
    print(bz, "/", bm, sep='')
else:
    bz = ipt - bcnt
    bm = i - bz + 1
    print(bz, "/", bm, sep='')
    pass
