array = ["1", "2", "3", "Abc", "def", "hij"]
print(array)

print(array[0])
print(array[5])

##배열은 0번째부터 5번째 까지이다

##이제 삽입을 해보자

array.append("Tom")
print(array)

## "배열이름".append(값) -> 배열(리스트)의 끝에 삽입한다 (즉 여기서는 6번 주소)
print("\n")
##그러면 제대로 해보자 ([6] = Tom이 있다는 가정하에 [3]에다가 Diana를 넣는다고 가정해보자)

array.append(None) ## [7] = None

array[7] = array[6]
array[6] = None
print(array)

array[6] = array[5]
array[5] = None
print(array)

array[5] = array[4]
array[4] = None
print(array)

array[4] = array[3]
array[3] = None
print(array)

array[3] = "Diana"
print(array)


##그럼 삭제는 어떻게 할까? (여기서 ABc를 지우겠다)

