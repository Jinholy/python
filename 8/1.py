input = int(input())

i = 1
while True:
    if input <= 1:
        break

    input = input-(6*i)
    i += 1

print(i)
