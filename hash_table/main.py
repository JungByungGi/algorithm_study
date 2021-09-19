import hashlib

# 해쉬 테이블 만들기
hash_table = list([i for i in range(10)])
print(hash_table)


# 해쉬 함수 만들기(나누기 방식)
def hash_func(key):
    return key % 5


# 해쉬 테이블 저장
data1 = 'Andy'
data2 = 'July'
data3 = 'Trump'
# ord : 문자의 아스키 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))  # 키 값 : 65, 데이터 값 : 0


# data:value 와 같이 data 와 value 를 넣으면, 해당 data 에 대한 key 를 찾아서, 해당 key 에
# 대응하는 해쉬주소에 value 를 저장하는 예
def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


storage_data('Andy', '01011112222')
storage_data('Dave', '01022223333')
storage_data('Trump', '01033334444')

print(hash_table)


# 해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print(get_data('Andy'))

# 리스트 변수를 활용해서 해시 테이블 구현
hash_table_v2 = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_func(get_key(data))
    hash_table_v2[hash_address] = value


def read_data(data):
    hash_address = hash_func(get_key(data))
    return hash_table_v2[hash_address]


save_data('Dave', '0102030200')
save_data('Andy', '01033232200')

print(read_data('Dave'))
print(hash_table_v2)

# chaining 기법
hash_table_chain = list([0 for i in range(8)])


def get_key_chain(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)
    #return hash(data)


def hash_function_chain(key):
    return key % 8


def save_data_chain(data, value):
    index_key = get_key_chain(data)
    hash_address = hash_function_chain(index_key)
    if hash_table_chain[hash_address] != 0:
        # 고려 사항은 링크드 리스트 대신 파이선에서는 리스트를 활용하여 자료구조를 나타낼 수 있다는 점이다.
        for index in range(len(hash_table_chain[hash_address])):
            if hash_table_chain[hash_address][index][0] == index_key:
                hash_table_chain[hash_address][index][1] = value
                return
        hash_table_chain[hash_address].append([index_key, value])
    else:
        hash_table_chain[hash_address] = [[index_key, value]]


def read_data_chain(data):
    index_key = get_key_chain(data)
    hash_address = hash_func(index_key)

    if hash_table_chain[hash_address] != 0:
        for index in range(len(hash_table_chain[hash_address])):
            if hash_table_chain[hash_address][index][0] == index_key:
                return hash_table_chain[hash_address][index][1]
        return None

    else:
        return None

    return hash_table_chain[hash_address]


save_data_chain('db', '11111')
save_data_chain('dn', '1111111111')


print("chaining 기법")
print(read_data_chain('db'))
print(hash_table_chain)

# Linear Probing 기법
hash_table_linear = list([0 for i in range(8)])


def get_key_linear(data):
    return hash(data)


def hash_function_linear(key):
    return key % 8


def save_data_linear(data, value):
    index_key = get_key_linear(data)
    hash_address = hash_func(index_key)
    if hash_table_linear[hash_address] != 0:
        # 해당 해시 주소에 값이 있으면 그 다음부터 데이터를 순회해야 한다.
        for index in range(hash_address, len(hash_table_linear)):
            if hash_table_linear[index] == 0:
                hash_table_linear[index] = [index_key, value]
                return
            # 동일한 키가 있는 경우 새 값을 업데이트 한다.
            elif hash_table_linear[index][0] == index_key:
                hash_table_linear[index][1] = value
                return
    else:
        hash_table_linear[hash_address] = [index_key, value]


def read_data_linear(data):
    index_key = get_key_chain(data)
    hash_address = hash_func(index_key)

    if hash_table_linear[hash_address] != 0:
        for index in range(hash_address, len(hash_table_linear)):
            if hash_table_linear[index] == 0:
                return None

            elif hash_table_linear[index][0] == index_key:
                return hash_table_linear[index][1]
    else:
        return None


save_data_linear('dk', '01200123123')
save_data_linear('da', '33333333333')

print(read_data_linear('da'))

# SHA-1 -> 해시 함수 대신 적용하면 될 듯
# data = 'test'.encode()
# hash_object = hashlib.sha1()
# hash_object.update(b'test')
# hex_dig = hash_object.hexdigest()
# print(hex_dig) # 항상 동일한 해시값
