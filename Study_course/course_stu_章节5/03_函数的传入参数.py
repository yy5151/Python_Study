"""
传参的功能是在函数进行计算的时候,接收外部调用时提供的数据
"""

# 定义一个带有参数的函数体
def sum(X,Y):
    result = X +Y
    print(f"{X}+{Y}的结果是:{result}")

# 定义两个外部传入参数
sum(X = int(input("请输入第一个数字")),Y = int(input("请输入第二个数字")))