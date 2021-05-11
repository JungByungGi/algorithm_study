import queue

## 일반 큐 ##
data_queue = queue.Queue()
data_queue.put("funcoding")
data_queue.put(1)
print(data_queue.qsize())  # 큐 사이즈 : 2
print(data_queue.get())  # 앞의 데이터 출력 : funcoding
print(data_queue.qsize())  # 사이즈 : 1

## Lifo 큐 ##
lifo_queue = queue.LifoQueue()
lifo_queue.put("funcoding")
lifo_queue.put(1)
print(lifo_queue.qsize())  # 큐 사이즈 : 2
print(lifo_queue.get())  # 앞의 데이터 출력 : 1(LIFO이므로)

## Priority 큐 ##
priority_queue = queue.PriorityQueue()
priority_queue.put((10, "Korea"))  # 튜플을 이용하여 (우선순위, 데이터) 형식으로 데이터 넣음
priority_queue.put((5, 1))
priority_queue.put((15, "China"))
print(priority_queue.qsize())  # 큐 사이즈 : 3
print(priority_queue.get())  # 우선 순위가 가장 빠른 1이 튜플 형태로 출력
print(priority_queue.get())  # 다음 우선 순위인 korea 출력

data_list = list()


# 리스트를 이용한 enqueue 구현
def enqueue(data):
    data_list.append(data)


# 리스트를 이용한 dequeue 구현
def dequeue():
    data = data_list[0]
    del data_list[0]
    return data


for i in range(10):
    enqueue(i) # 0~9R까지 자연수
print(data_list)
print(dequeue()) # 0
print(dequeue()) # 1