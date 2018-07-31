# 배열 미리 잡아놓으면 메모리초과뜨고 할때마다 구하게 하면 시간초과뜸
def get_factorial(var, rng):
    result = 1
    for i in range(var, var - rng, -1):
        result *= i

    return result


cmd_input = []

while True:
    ipt = input()
    if ipt == '0 0':
        break
    cmd_input.append(ipt)

result_lst = []
for i in cmd_input:
    a, b = map(int, i.split(' '))
    result = get_factorial(a, b) // get_factorial(b, b)
    result_lst.append(result)

print('\n'.join(map(str, result_lst)))
