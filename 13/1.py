class deque():
    def __init__(self):
        self.m_list = []
        self.m_size = 0

    def push_front(self, var):
        tmp = []
        tmp.append(var)
        for v in self.m_list:
            tmp.append(v)
        self.m_list = tmp
        self.m_size += 1

    def push_back(self, var):
        self.m_list.append(var)
        self.m_size += 1

    def pop_back(self):
        if self.m_size == 0:
            return -1
        self.m_size -= 1
        return self.m_list.pop()

    def pop_front(self):
        if self.m_size == 0:
            return -1
        tmp = self.m_list[0]
        self.m_list.remove(tmp)
        self.m_size -= 1
        return tmp

    def size(self):
        return self.m_size

    def front(self):
        if self.m_size == 0:
            return -1
        return self.m_list[0]

    def back(self):
        if self.m_size == 0:
            return -1
        return self.m_list[self.m_size - 1]

    def empty(self):
        if self.m_size == 0:
            return 1
        else:
            return 0


d = deque()
ipt = int(input())
cmd_list = []
result = []
for i in range(ipt):
    cmd_list.append(input())

for att in cmd_list:
    try:
        a, b = att.split(' ')
    except:
        a = att

    if a == 'push_front':
        d.push_front(b)
    elif a == 'push_back':
        d.push_back(b)
    elif a == 'pop_front':
        print(d.pop_front())
    elif a == 'pop_back':
        print(d.pop_back())
    elif a == 'size':
        print(d.size())
    elif a == 'empty':
        print(d.empty())
    elif a == 'front':
        print(d.front())
    else:  # back
        print(d.back())
