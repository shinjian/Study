# 0 ~ A-1
# range(A)

# A ~ B-1
# range(A, B)

# A ~ B-1 -C
# range(A, B, C)

print(range(5))
print(list(range(10)))
print(list(range(0, 5)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))
print(list(range(0, 10+1)))

n = 10
# print(range(0, n/2))      TypeError
print(range(0, int(n/2)))
print(range(0, n//2))