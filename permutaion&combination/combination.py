import time
from itertools import combinations

comb = []

items = list(range(1000))

# itertools 순열
print('itertools의 조합')

start1 = time.time()

for i in list(combinations(items, 2)):
    pass

print("조합 연산 측정 시간1 : %f" % (time.time() - start1))

# 재귀를 이용한 조합
print('\n재귀 조합')


def combinations(data, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(data)):
        elem = data[i]
        rest_elem = data[i + 1:]
        for c in combinations(rest_elem, n - 1):
            result.append([elem] + c)

    return result

start2 = time.time()
combinations(items, 2)
print("조합 연산 측정 시간2 : %f" % (time.time() - start2))