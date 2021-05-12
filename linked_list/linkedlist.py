class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 링크드 리스트를 관리 하는 클래스(NodeManagement)
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    # 데이터 추가
    def add(self, data):
        if self.head == '':
            self.head == Node(data)
        else:
            # head 부터 검사
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 링크드리스트 데이터 출력 함수
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


linkedlist = NodeMgmt(0)
# linkedlist.desc()
for data in range(1, 20):
    linkedlist.add(data)
linkedlist.desc()
