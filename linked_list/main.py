# 링크드 리스트 노드 구현 #
class Node:
    def __init__(self, data, next=None):
        self.data = data  # data
        self.next = next  # 포인터


# 링크드 리스트로 데이터 추가하기
def add(data):
    # 가장 앞에 있는 노드
    node = head
    # 마지막 노드를 찾기 위함(node.next가 없으니까 node가 맨 앞임을 의미)
    while node.next:
        node = node.next

    # null 인 노드에 생성한 노드 추가
    node.next = Node(data)


# 링크드 리스트 데이터 출력
node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

node = head
while node.next:
    print(node.data) # 1~8까지
    node = node.next # 출력하고 다음 노드로 넘어가야 함.
# 마지막 노드의 데이터 값
print(node.data)