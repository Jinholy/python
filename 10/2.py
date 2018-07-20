def is_prime_num(num):
    ipt = int(num)

    for i in range(2, ipt):
        if num % i == 0:
            return False
    if num == 1 or num == 0: return False
    return True


X = int(input())
Y = int(input())

result = 0
lst = []
for i in range(X, Y+1):
    if is_prime_num(i):
        lst.append(i)

if len(lst) == 0:
    print('-1')
else:
    print(sum(lst))
    print(lst[0])

