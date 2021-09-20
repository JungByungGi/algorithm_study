bubble_list = [5, 1, 9, 7, 2, 3]


def bubble_sort(data):
    count = 0
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - i - 1):
            # 한 번도 swap이 일어나지 않았다는 것은 이미 정렬되어 있는 상태
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                count += 1
                swap = True
        # 최적화를 위해서 바로 for문 break
        if not swap:
            break


bubble_sort(bubble_list)
print(bubble_list)
