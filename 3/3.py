#별찍기

'''
N = int(input())

for i in range(1,N+1):
    print("*" * i)
'''

'''
N = int(input())

for i in range(1, N + 1):
    if i != N:
        print(" " * (N - i -1), "*" * i)
    else:
        print("*"*i)

'''


'''
N = int(input())

for i in range(1, N + 1):
   print("*"*(N-i+1))
'''


N = int (input())

for i in range(1, N+1):
    if i == 1:
        print("*"*N)
    else:
        print(" "*(i-2), "*"*(N-i+1))
