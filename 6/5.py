score = []

for i in range(0, 5):
    sc = int(input())
    if sc < 40:
        score.append(40)
    else:
        score.append(sc)


print(int(sum(score)/5))
