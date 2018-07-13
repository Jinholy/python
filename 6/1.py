ipt = input()

arr = ipt.split(' ')

try:
    while True:
        arr.remove('')
except:
    pass

count = len(arr)
print(count)
