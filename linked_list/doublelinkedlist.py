class Node:
    # 더블 링크드리스트는 주소가 2개
    def __init__(self, data, prev=None, next=None):
        self.next = next
        self.prev = prev
        self.data = data


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)  # 맨 앞 노드
        self.tail = self.head  # 맨 뒤 노드

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head is None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head is None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    # 특정 노드 뒤에 노드 추가하는 함수
    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node is None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True

    def insert_after(self, data, after_data):

        if self.head is None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node is None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next is None:
                self.tail = new
            return True


double_linkedlist = NodeMgmt(0)
for data in range(1, 10):
    double_linkedlist.insert(data)
double_linkedlist.desc()

# 이중 연결 리스트 데이터 머리부터 검색
print("데이터 머리부터 검색")
print(double_linkedlist.search_from_head(9).data)
node3 = double_linkedlist.search_from_head(100)
if node3:
    print(node3.data)
else:
    print("no")

# 이중 연결 리스트 데이터 꼬리부터 검색
print("데이터 꼬리부터 검색")
print(double_linkedlist.search_from_head(9).data)
node3 = double_linkedlist.search_from_head(100)
if node3:
    print(node3.data)
else:
    print("no")

# 이중 연결 리스트 중간에 데이터 추가
print("이중 연결 리스트 기존 데이터")
double_linkedlist.desc()
double_linkedlist.insert_before(1.5, 2)
print("이중 연결 리스트 데이터 추가한 이후 데이터")
double_linkedlist.desc()

print("이중 연결 리스트 기존 데이터")
double_linkedlist.desc()
double_linkedlist.insert_after(2.5, 2)
print("이중 연결 리스트 데이터 추가한 이후 데이터")
double_linkedlist.desc()