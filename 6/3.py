num = int(input())
ox_cases = []

for i in range(0, num):
    ox_cases.append(input().split('X'))


def get_score(i):
    score = 0
    for s in range(0, i + 1):
        score += s

    return score


total_score = []
for case in ox_cases:
    score = 0
    for o in case:
        score += get_score(len(o))

    total_score.append(score)


for i in total_score:
    print(i)