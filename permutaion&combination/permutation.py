from itertools import permutations
import time

perm = []

items = list(range(1000))

# itertools 순열
print('itertools의 순열')

start1 = time.time()
for i in list(permutations(items, 2)):
    pass

print("순열 연산 측정 시간1 : %f" % (time.time() - start1))


# 재귀를 이용한 순열
print('재귀 순열')


def permutations(data, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(data):
        for p in permutations(data[:i] + data[i + 1:], n - 1):
            result += [[elem] + p]

    return result


start2 = time.time()
permutations(items, 2)
print("순열 연산 측정 시간2 : %f" % (time.time() - start2))
