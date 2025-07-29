"""
序列的切片：从一个序列中，取出一个子序
语法：序列【起始下标：结束下标：步长】
"""
# 对list进行切片，从1开始，4结束，步长为1
my_list = [1,2,3,4,5,6]
result = my_list[1:4]   # 步长默认是1，所以可以省略不写
print(f"结果1：{result}")

# 对tuple进行切片，从头开始到尾结束，步长为1
my_tuple = (0,1,2,3,4,5)
result2 = my_tuple[:]  # 起始和结束不写表示从头到尾，步长为1可以省略
print(f"结果2：{result2}")

# 对str进行切片，从头开始到尾结束，步长为2
my_str = "012345678"
result3 = my_str[::2]
print(f"结果3：{result3}")

# 对str进行切片，从头开始到尾结束，步长为-1
my_str = "012345678"
result4 = my_str[::-1] # 等同于将序列反转
print(f"结果3：{result4}")


# 练习案例，取出字符串“黑马程序员”
str = "万过薪月，员序程马黑来，nohtyP学"
# 倒序取
r1 = str[5:10]
print(r1[::-1])

# split函数
r2 = str.split("，")
r3 = r2.pop(1).replace("来","")
print(r3[::-1])