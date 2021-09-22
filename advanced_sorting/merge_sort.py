def merge_split(data):
    if len(data) <= 1:
        return data

    split_index = len(data) // 2
    left = merge_split(data[:split_index])
    right = merge_split(data[split_index:])
    return merge_sort(left, right)


def merge_sort(left_list, right_list):
    result = list()
    left_index, right_index = 0, 0  # d

    # case1 : left/right이 남아있을 때
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] > right_list[right_index]:
            result.append(right_list[right_index])
            right_index += 1
        else:
            result.append(left_list[left_index])
            left_index += 1

    # case2 : left만 남아 있을 때
    while left_index < len(left_list):
        result.append(left_list[left_index])
        left_index += 1

    # case3 : right만 남아 있을 때
    while right_index < len(right_list):
        result.append(right_list[right_index])
        right_index += 1

    return result


unsorted_list = [5, 6, 2, 1, 7, 8, 11, 14]
print(merge_split(unsorted_list))
