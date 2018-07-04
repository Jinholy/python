f1 = open("text.txt", 'w')
f1.write("ㅇ아오러옹ㄹ")
f1.close()

f2 = open("text.txt", 'r')
print(f2.read())
f2.close()

