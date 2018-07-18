ipt = int(input())
st = set()

for i in range(ipt):
    st.add(int(input()))

st = sorted(st)

for i in st:
    print(i)

