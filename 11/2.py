class stack:
    def __init__(self):
        self.lst = []
        self.length = 0

    def pop(self):
        if self.length == 0:
            return -1

        self.length -= 1
        return self.lst.pop()

    def push(self, var):
        self.length += 1
        self.lst.append(var)

    def size(self):
        return self.length

    def empty(self):
        if self.length == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.length == 0:
            return -1

        return self.lst[self.length - 1]


size = int(input())
lst = []
stk = stack()

for i in range(size):
    lst.append(input())

for i in lst:
    stk = stack()
    flag = True
    for idx in range(len(i)):
        if i[idx] == '(':
            stk.push(i[idx])
        else:
            if stk.pop() == -1:
                print("NO")
                flag = False
                break

    if stk.size() == 0 and flag:
        print("YES")
    elif flag:
        print("NO")
