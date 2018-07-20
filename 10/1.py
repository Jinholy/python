def is_prime_num(num):
    ipt = int(num)

    for i in range(2, ipt):
        if num % i == 0:
            return False
    if num == 1 or num == 0: return False
    return True


ipt = int(input())

lst = list(map(int, input().split(' ')))

cnt = 0

for i in lst:
    if is_prime_num(i):
        cnt += 1

print(cnt)
