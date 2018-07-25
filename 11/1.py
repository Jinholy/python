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
stack = stack()

cmd_lst = []

for i in range(size):
    cmd_lst.append(input())

for i in cmd_lst:
    try:
        a, b = i.split(' ')
    except:
        a = i

    if a == 'push':
        stack.push(int(b))
    elif a == 'top':
        print(stack.top())
    elif a == 'size':
        print(stack.size())
    elif a == 'pop':
        print(stack.pop())
    else:
        print(stack.empty())
