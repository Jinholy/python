ipt = int(input())
lst = []

def bm(num):
    if num < 10:
        return '0'+str(num)

    return num

for i in range(ipt):
    lst.append(input())

for i in lst:
    H, W, N = map(int, i.split(' '))
    if N%H != 0 :
        print(N % H, bm(N // H+1), sep='')
    else:
        print(H,bm(N//H), sep='')

