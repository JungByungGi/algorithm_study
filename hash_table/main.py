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
