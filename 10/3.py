arr = [True] * 1000000
arr[0] = False
arr[1] = False

a, b = map(int, input().split(' '))

for i in range(len(arr)):
    if arr[i]:
        k = 2
        while True:
            if i*k >= 1000000:
                break
            arr[i * k] = False
            k += 1

for i in range(a, b+1):
    if arr[i]:
        print(i)


#X, Y = map(int, input().split())
