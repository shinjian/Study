# [element]
array = [273, 32, 103, "String", True, False]
print(array)
print()

# 273[0]  32[1]  103[2]  String[3]  True[4]  False[5]
list_a = [273, 32, 103, "String", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print()

# element change
list_a[0] = "Change"
print(list_a)
print()

print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
print()

print(list_a[3])
print(list_a[3][0])

list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_b[1])
print(list_b[1][1])

# IndexError
list_c = [273, 32, 103]
print(list_c[3])