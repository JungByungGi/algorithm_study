def binary_search(data, search):
    data.sort()
    if len(data) == 1 and search == data[0]:
        return True

    if len(data) == 1 and search != data[0]:
        return False

    # 방어 코드
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)


list = [2, 3, 4, 1, 3, 11, 35, 78]

print(binary_search(list, 111))
