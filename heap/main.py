# 그림 그리면서 원리 파악하기
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2

        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # 1. 왼쪽 자식 노드가 없는 경우
        if left_child_popped_idx >= len(self.heap_array):
            return False

        # 2. 왼쪽은 있는데 오른쪽 자식 노드는 없는 경우
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False

        # 3. 자식 노드가 둘 다 있는 경우(자식 노드의 크기를 먼저 비교하고 그 후에 부모 노드와 비교)
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False

    def insert(self, data):
        # 힙은 완전 이진 트리이므로 append로 데이터를 넣어줘도 됨.
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        # 맨 밑부터 올라가면서 비교
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            inserted_idx = parent_idx

        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]  # 필요 없는 데이터는 삭제
        popped_idx = 1

        # 루트부터 내려가면서 비교
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            # 3. 자식 노드가 둘 다 있는 경우(자식 노드의 크기를 먼저 비교하고 그 후에 부모 노드와 비교)
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
                        self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx],self.heap_array[right_child_popped_idx]
                        popped_idx = right_child_popped_idx
        # 값을 덮어 씌울 것이기 때문에 별도로 삭제할 필요 없음.
        return returned_data


# test
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array) # [None, 20, 10, 15, 5, 4, 8]
heap.pop()
print(heap.heap_array) # [None, 15, 10, 8, 5, 4]
heap.pop()
print(heap.heap_array) # [None, 10, 5, 8, 4]
