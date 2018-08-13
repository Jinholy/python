pibo_arr = []


def get_pibo(n):
    pibo_arr.append(0)
    if n == 0:
        pibo_arr[n] = 0
    elif n == 1:
        pibo_arr[n] = 1
    else:
        pibo_arr[n] = pibo_arr[n - 1] + pibo_arr[n - 2]


ipt = int(input())
max_int = 0
result_cmd = []

for i in range(ipt):
    cmd_ipt = int(input())
    result_cmd.append(cmd_ipt)
    if cmd_ipt > max_int:
        max_int = cmd_ipt

for i in range(max_int + 1):
    get_pibo(i)

for i in result_cmd:
    if i == 0:
        print(1, 0)
    elif i == 1:
        print(0, 1)
    else:
        print(pibo_arr[i - 1], pibo_arr[i])
