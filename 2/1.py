acc = []
out = ''
while True:
    try:
        acc.append(input('')) # Or whatever prompt you prefer to use.
    except EOFError:
        out = '\n'.join(acc) #리스트 사이사이에 엔터넣어줌!
        break

for s in acc:
    print(s)

'''
f = open("input.txt", 'r')
strs = []

while True:
    f_input = f.read()
    if f_input =='':
        break
    else:
        strs.append(f_input)


for s in strs:
   print(s)

f.close()
'''


'''
s = []

while True:
    input_data = input()

    if input_data == '' or input_data == '^Z':
        break
    else:
      s.append(input_data)


for str in s:
    print(str)
'''