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

    # 링크드리스트 데이터 삭제
    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없다.")
            return
        # 헤더 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        # 중간 및 마지막 노드 삭제
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    # 노드 검색
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next


# 링크드 리스트 데이터 추가 확인
'''
linkedlist = NodeMgmt(0)
# linkedlist.desc()
for data in range(1, 20):
    linkedlist.add(data)
linkedlist.desc()
'''

# 링크드 리스트 데이터 삭제 확인
linkedlist1 = NodeMgmt(1)
print(linkedlist1.head)
linkedlist1.delete(1)
print(linkedlist1.head)

linkedlist1 = NodeMgmt(1)
print(linkedlist1.head)
for data in range(2, 10):
    linkedlist1.add(data)
linkedlist1.desc()
print("데이터 4 삭제 후")
linkedlist1.delete(4)
linkedlist1.desc()
print("데이터 9 삭제 후")
linkedlist1.delete(9)
linkedlist1.desc()
print(linkedlist1.search_node(8).data) # 노드 검색
