str = input("저장할 내용을 입력하세요:")
f = open("test.txt", 'w')
f.write(str)
f.close()