def quick_sort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list()
    pivot = data[0]

    # for i in range(1, len(data)):
    #     if pivot <= data[i]:
    #         right.append(data[i])
    #     else:
    #         left.append(data[i])

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quick_sort(left) + [pivot] + quick_sort(right)


unsorted_list = [5, 6, 2, 1, 7, 8, 11, 14]
print(quick_sort(unsorted_list))
