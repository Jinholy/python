import sys

str = input()

idx = 0
for i in range(0, len(str)):
    sys.stdout.write(str[i])
    idx = idx + 1
    if idx == 10:
        print()
        idx = 0



