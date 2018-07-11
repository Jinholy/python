def get_num(old):
    tmp = old%10
    new = int(old/10) + int(old%10)
    return int(str(tmp) + str(new%10))

num = int(input())
tmp = get_num(num)
count = 1
while True:
    if tmp == num:
        break
    tmp = get_num(tmp)
    count = count + 1


print(count)
