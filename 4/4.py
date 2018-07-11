def get_result(v, m, n):
    result = 0
    for i in v:
        result = result + i / M * 100

    return result/n


N = int(input())
vars = list(map(int, input().split(' ')))

vars.sort()
M = vars[N - 1]

print(get_result(vars, M, N))


