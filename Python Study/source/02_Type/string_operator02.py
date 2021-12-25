# Python zero index
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

# [] - indexing
# [:] - slicing

print("안녕하세요"[1:4]) # index 1 ~ 4 output
print("안녕하세요"[0:2]) # index 0 ~ 2 output
print("안녕하세요"[1:3]) # index 1 ~ 3 output
print("안녕하세요"[2:4]) # index 2 ~ 4 output

print("안녕하세요"[1:]) # index 1 ~ output
print("안녕하세요"[:3]) # index ~ 3 output

# len - 문자열의 길이
print(len("안녕하세요"))