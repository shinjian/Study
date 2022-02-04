# isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
# isalpha() : 문자열이 알파벳으로만 구성되어 있는지 확인
# isidentifier() : 문자열이 식별자로 사용할 수 있는 것인지 확인
# isdecimal() : 문자열이 정수 형태인지 확인
# isdigit() : 문자열이 숫자로 인식될 수 있는 것인지 확인
# isspace() : 문자열이 공백으로만 구성되어 있는지 확인
# islower() : 문자열이 소문자로만 구성되어 있는지 확인
# isupper() : 문자열이 대문자로만 구성되어 있는지 확인
# boolean(True or False)

print("TrainA10".isalnum())     # True
print("TrainA10!".isalnum())    # False

print("ABC".isalpha())          # True
print("ABC10".isalpha())        # False

print("10".isdigit())           # True
print("10a".isdigit())          # False