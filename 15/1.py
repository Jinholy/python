def get_factorial(var, rng):
    result = 1

    for i in range(var, var - rng, -1):
        result *= i

    return result


a, b = map(int, input().split(' '))
result = get_factorial(a, b) // get_factorial(b, b)
print(result)
#print(result % 10007) #문제 2번
