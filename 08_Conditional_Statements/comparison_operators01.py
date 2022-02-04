# == 같다               != 다르다
# > 크다                < 작다
# >= 크거나 같다        <= 작거나 같다

print(10 == 100)    # 10과 100은 같다 (False)
print(10 != 100)    # 10과 100은 다르다 (True)
print(10 < 100)     # 10은 100보다 작다 (True)
print(10 > 100)     # 10은 100보다 크다 (False)
print(10 <= 100)    # 10은 100보다 작거나 같다 (True)
print(10 >= 100)    # 10은 100보다 크거나 같다 (False)
print()

# 문자열은 사전 순서로 앞에 있는 것이 작은 값을 가짐
print("가방" == "가방")     # True
print("가방" != "하마")     # True
print("가방" < "하마")      # True
print("가방" > "하마")      # False
print()

x = 25
print(10 < x < 30)      # True
print(40 < x < 60)      # False