s = []

value = ""
while True:
    value = input()
    if value == "":
        break
    else:
        s.append(value)

sum = 0
for val in s:
    sum = sum + int(val)

print(sum/s.__len__())
