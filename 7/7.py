lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()

for i in lst:
    str = str.replace(i, '*')
#    print(str.find(i))

print(len(str))
