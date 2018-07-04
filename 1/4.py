#이 파일의 내용중 java라는 문자열을 python으로 바꾸어서 저장하시오.
f = open("test.txt", 'w')
f.write("life is too short\n")
f.write("you need java")
f.close()


f = open("test.txt", 'r')

str = []
while True:
    line = f.readline()
    str.append(line.replace("java", "python"))
    if line == "":
        break
f.close()



f = open("test.txt", 'w')

for s in str:
    f.write(s)

f.close()



