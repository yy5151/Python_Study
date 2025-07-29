"""
for 循环相当于遍历循环,无法构建无限循环
for 临时变量 in 待处理数据集(序列):
    循环满足条件时执行的代码
"""

# 一个一个打印字符串中的字母
name = "itheima"
for x in name:
    print(x)

s = "itheima is a brand of itcast"
n = 0
for x in s:
    if x == "a":
        n += 1
print(n)
