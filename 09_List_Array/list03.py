# list_name.append(element)
# list_name.insert(position, element)
# list_name.extend([element])

# 리스트를 선언
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가
print("# 리스트 뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가
print("# 리스트 중간에 요소 추가")
list_a.insert(0, 10)
print(list_a)
print()

# 리스트 여러 요소 추가
print("# 리스트 여러 요소 추가")
list_a.extend([4, 5, 6])
print(list_a)