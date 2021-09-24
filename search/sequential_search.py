from random import *

rand_data_list = list()
for num in range(10):
    rand_data_list.append(randint(1, 100))


def sequential_search(data, search):
    for index in range(len(data)):
        if data[index] == search:
            return True
    return False


print(rand_data_list)
print(sequential_search(rand_data_list, 4))
