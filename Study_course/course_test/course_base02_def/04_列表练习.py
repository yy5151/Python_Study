age = [21,25,21,23,22,20]

# 追加一个数字31到列表的尾部
age.append(31)
print(age)

# 追加一个新列表[29,33,30],到列表的尾部
age.extend([29,33,30])
print(age)

# 取出第一个元素
first = age.pop(0)
print(first)

# 取出最后一个元素
last = age.pop(-1)
print(last)

# 查找元素31，在列表中的下标位置
index = age.index(31)
print(index,age)