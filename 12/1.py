class queue():
    def __init__(self):
        self.q_size = 0
        self.lst = []

    def push(self, var):
        self.lst.append(var)
        self.q_size += 1

    def pop(self):
        if self.q_size == 0:
            return -1

        result = self.lst[0]
        self.lst.remove(self.lst[0])
        self.q_size -= 1
        return result

    def size(self):
        return self.q_size

    def empty(self):
        if self.q_size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.q_size == 0:
            return -1
        else:
            return self.lst[0]

    def back(self):
        if self.q_size == 0:
            return -1

        return self.lst[self.q_size-1]


size = int(input())
lst = []
queue = queue()

for i in range(size):
    lst.append(input())

for i in lst:
    try:
        a, b = i.split(' ')
    except:
        a = i

    if a == 'push':
        queue.push(b)
    elif a == 'pop':
        print(queue.pop())
    elif a == 'size':
        print(queue.size())
    elif a == 'empty':
        print(queue.empty())
    elif a == 'front':
        print(queue.front())
    elif a == 'back':
        print(queue.back())
    else:
        pass
