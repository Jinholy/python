class paper():
    def __init__(self, priority):
        self.p_priority = priority
        self.print_this = False

    def get_priority(self):
        return self.p_priority

    def get_print_this(self):
        return self.print_this

    def set_print_this_true(self):
        self.print_this = True


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

        return self.lst[self.q_size - 1]

    def push_back(self, paper):
        self.lst.append(paper)
        self.q_size += 1

    def get_lst(self):
        return self.lst


class printer(queue):
    def __init__(self, p_queue):
        self.p_queue = p_queue
        self.max_priority = 0

    def make_print(self, paper):
        q = self.p_queue
        len = self.p_queue.size()
        cnt = 1
        for i in range(len):
            tmp = q.pop()
            if tmp.get_priority() < self.max_priority:
                q.push_back(tmp)
            else:
                if tmp.get_print_this():
                    break
                self.set_m_priority()
                cnt += 1

        return cnt

    def push_print(self, document):
        p = document.get_priority()
        if p > self.max_priority:
            self.max_priority = p

        self.p_queue.push(document)

    def set_m_priority(self):
        lst = self.p_queue.get_lst()
        result = 0
        for i in lst:
            p = i.get_priority()
            if result < p:
                result = p

        self.max_priority = result


size = int(input())
case_a = []
case_b = []
for i in range(size):
    case_a.append(input())
    case_b.append(input())

for i in range(size):
    a, b = map(int, case_a[i].split(' '))
    q = queue()
    p = printer(q)
    paper_to_print = None
    lst = list(map(int, case_b[i].split(' ')))
    cnt = 0
    for k in lst:
        if cnt == b:
            paper_to_print = paper(k)
            paper_to_print.set_print_this_true()
            q.push(paper_to_print)
        else:
            q.push(paper(k))
        cnt += 1

    p.set_m_priority()
    print(p.make_print(paper_to_print))


#답안나옴 ㅅㄱ
