f = open('nums.txt', 'w')

for i in range(1, 21542):
    if i % 100 == 0:
        f.write(str(i)+"\n")
    else:
        f.write(str(i) + ',')

f.close()
