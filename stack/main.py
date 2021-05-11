# 함수 호출 시 프로세스 실행 구조를 스택과 비교해서 이해하기
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)


recursive(4)  # 재귀 함수 호출 시 스택 구조로 쌓임.

# 파이썬 메소드 사용
data_stack = list()
data_stack.append(1)
data_stack.append(2)

print(data_stack)  # [1, 2]

print(data_stack.pop())  # 스택이므로 2가 먼저 출력

# push, pop 함수 구현
stack_list2 = list()


# push 함수 구현
def push(data):
    stack_list2.append(data)


# pop 함수 구현
def pop():
    data = stack_list2[-1]
    del stack_list2[-1]
    return data


for index in range(10):
    push(index)

print(stack_list2) # 0~9
print(pop()) # 9 출력
