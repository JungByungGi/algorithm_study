# 동적 계획법 활용
def fibo_dp(num):
    cache = [0 for i in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, num + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[num]


print(fibo_dp(10))
