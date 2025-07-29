"""
学习字符串的相关操作
"""
str = "itheima and itcast"
# 通过下标索引取值
value1 = str[2]
value2 = str[-16]
print(f"从字符串{str}取出下标为2的元素，值是：{value1},取出下标为-16的元素，值是：{value2}")
name = "itheima"
print(name[0])
print(name[-1])
# 尝试修改指定下标的字符
# name[0] = "a",报错字符串无法修改，

# idex方法
value = str.index("and")
print(f"在字符串{str}中查找and,其起始下标是：{value}")


"""
字符串的替换
语法：字符串.replace(字符串1，字符串2)
功能：将字符串内的全部：字符串1，替换为字符串2
注意：不是修改字符串本身，而是得到一个新字符串
"""

# replace方法
new_str = str.replace("it","程序")
print(f"旧字符串：{str},修改后：{new_str}")


"""
字符串的分割
语法：字符串.split(分隔符)
功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
注意:字符串本身不变，而是得到了一个列表对象
"""

my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")# 按照空格将字符串分割
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是：{type(my_str_list)}")


"""
去除字符串前后指定字符
语法：字符串.strip(指定字符)
注意：指定字符是两个时，只要字符串前后含有指定字符，无论什么顺序都会被去除
"""
new_str = " itheima and itcast "
# 去除字符串前后的空格
print(new_str.strip(),type(new_str.strip()))

two_new_str = "12itheima and itcast21"
# 去除字符串前后含有“2”，“1”两个字符
print(two_new_str.strip("12"))

# 统计字符串中某字符串的出现次数，count
str = "itheima and itcast"
count = str.count("it")
print(f"字符串{str}中“it”出现了{count}次")


# 统计字符串的长度，len()
num = len(str)
print(f"len函数统计{str}的长度为：{num}")