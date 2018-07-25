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



input = input()
stk = stack()

for i in range(len(input)):
    stk.push(input[i])


