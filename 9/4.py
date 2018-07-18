ipt = int(input())

st = set()

for i in range(ipt):
    st.add(input())

lst = sorted(st, key=lambda x: (len(x), x))

print('\n'.join(lst))
