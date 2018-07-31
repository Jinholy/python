factorial_arr = []
factorial_arr.append(1)

for i in range(1, 501):
    factorial_arr.append(factorial_arr[i - 1] * i)


input = int(input())
result = factorial_arr[input]
cnt = 0
while True:
    if result % 10 != 0:
        break
    cnt += 1
    result = result // 10

print(cnt)
