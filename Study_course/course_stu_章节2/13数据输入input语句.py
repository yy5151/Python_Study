"""
input 语句接收键盘输入信息,并带有返回值
"""
print("你是谁?")
name=input()
print("我是%s"%name)

# input()语句本身可以在要求使用者输入内容前,输出提示内容
name = input("你叫啥名?")
print("我叫%s"%name)

# input()接收到的数据类型默认为字符串型
in_type=input("请输入数字")
print(type(in_type))

# 需要自行转换input()数据类型
age=int(input("你多大?"))
print(f"我今年{age}岁")