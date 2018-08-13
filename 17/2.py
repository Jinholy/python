cost_red = []
cost_green = []
cost_blue = []

ipt = int(input())
cmd_lst = []
for i in range(ipt):
    r, g, b = map(int, input().split(' '))
    cost_red.append(r)
    cost_green.append(g)
    cost_blue.append(b)

def get_lowest_cost(n, color):
    r = cost_red[i]
    g = cost_green[i]
    b = cost_blue[i]


last_color = 0  # 0:r 1:g 2:b
total_cost = 0
