insertion_list = [5, 1, 9, 7, 2, 3, 10, 11, 12]


def insertion_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
            # swap을 안 하면 이미 정렬이 되어 있다는 것
            else:
                break
    return data


print(insertion_sort(insertion_list))
