"""
返回值是程序中函数完成事情后,最终给调用者的结果

def 函数名(参数...)
    函数体
    return 返回值


变量 = 函数(参数)
"""

def sum(x,y):
    # 第二步执行14行,两数相加
    result = x+y
    # 得到result返回给函数调用
    return result# return 之后的代码不会被执行

# 先执行的19行,函数接收参数
r = sum(2,9)# 最后用变量r接收返回值,并打印
print(f"{r}")