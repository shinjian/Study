# 딕셔너리에 값 추가하기/제거하기
# dictionary[new key] = new value
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
dictionary["price"] = 5000
del dictionary["ingredient"]
print(dictionary)