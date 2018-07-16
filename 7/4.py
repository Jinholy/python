ipt = int(input())
lst = []


def is_group_word(str):
    tmp = str[0]
    cnt = 0
    for i in range(len(str)):
        c = list(str).count(tmp)
        if str[i] != tmp:
            if cnt != c:
                return False
            else:
                cnt = 0

        tmp = str[i]
        cnt += 1

    return True


for i in range(ipt):
    lst.append(input())

count = 0
for s in lst:
    if is_group_word(s):
        count += 1

print(count)
