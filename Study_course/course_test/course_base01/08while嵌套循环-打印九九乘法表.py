# 补充知识点

# print语句打印出来的内容会自动换行
print("hello")
print("word")
# 不换行输出
print("hello",end='')
print("word")
# 多行字符进行对齐,\t
print("hello \tword")
print("yuan \tying")

# 通过while循环输出九九乘法表
# 控制有多少行的外层循环
i = 1
while i <= 9:
    # 控制有多少个的内层循环
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}\t",end='')
        j += 1
    i +=1
    print()
