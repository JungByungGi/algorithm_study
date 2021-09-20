selection_list = [5, 1, 9, 7, 2, 3]


def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[min_idx], data[i] = data[i], data[min_idx]
    return data


print(selection_sort((selection_list)))
