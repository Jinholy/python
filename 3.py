#문자열 입력한거 파일에 저장하고 다시 읽어서 거꾸로 저장하기
string = []
while True:
    input_str = input()
    if input_str == "":
        break
    else:
        string.append(input_str)


f = open("abc.txt", 'w')

for str in string:
    f.write(str+'\n')

f.close()

f = open("abc.txt", 'r')
a = []
while True:
    line = f.readline()
    if not line: break
    a.append(line)
f.close()

print(a)
a.reverse()

f = open("abc.txt", 'w')

for str in a:
    f.write(str)
