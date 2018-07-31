# 아니 무슨 패르마의 소정리니 확장 유클리드 호제법이니 그런게 나와욧!
# 메모리초과, 틀림
# 결국 6번답으로 씀
factorial_arr = []
factorial_arr.append(1)

for i in range(1, 200):
    factorial_arr.append(factorial_arr[i - 1] * i)

a, b = map(int, input().split(' '))
result = factorial_arr[a] // factorial_arr[a - b] // factorial_arr[b]

print(result)
