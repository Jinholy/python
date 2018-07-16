from collections import Counter

ipt = list(input().lower())
ctr = Counter(ipt)
lst = sorted(ctr.values())

MAX_1 = lst[len(lst)-1]
MAX_2 = lst[len(lst)-2]

def get_key_by_val(val):
    key = ctr.keys()
    for i in key:
        if ctr[i] == val:
            return i

if  len(ctr) == 1:
    print(ipt[0].upper())
elif MAX_1 == MAX_2:
    print('?')
else:
    print(str(get_key_by_val(MAX_1)).upper())

