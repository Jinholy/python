#답안나옴ㅋㅋ
class c_queue():
    def __init__(self, size):
        self.m_list = []
        self.m_size = size
        for i in range(size):
            self.m_list.append(False)

    def pop(self):
        if self.m_size == 0:
            return -1
        tmp = self.m_list[0]
        self.m_list.remove(tmp)
        # self.m_size -= 1
        self.m_list.append(False)
        return tmp

    def push_right(self):
        tmp = self.m_list[self.m_size - 1]
        for i in range(self.m_size - 1, 0, -1):
            self.m_list[i] = self.m_list[i - 1]

        self.m_list[0] = tmp

    def push_left(self):
        tmp = self.m_list[0]
        self.m_list.remove(tmp)
        self.m_list.append(tmp)

    def set_attr(self, idx):
        if self.m_size < idx:
            return -1
        self.m_list[idx - 1] = True

    def front(self):
        return self.m_list[0]

    def turn_right_or_left(self):
        print("\nsm:", self.m_size // 2, sep='', end='')
        for i in range(self.m_size // 2 + 1):
            print(i, sep=' ', end='')
            if self.m_list[i]:
                return False

        return True


N, M = map(int, input().split(' '))
cq = c_queue(N)
true_list = list(map(int, input().split(' ')))

for i in true_list:
    cq.set_attr(i)

cnt = 0
result = 0
while True:
    if cnt == M:
        break

    if cq.front():
        cq.pop()
        cnt += 1
    elif cq.turn_right_or_left():
        cq.push_right()
        result += 1
    else:
        cq.push_left()
        result += 1

print(result)
