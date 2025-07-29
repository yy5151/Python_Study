"""
变量分为局部变量，全局变量
作用域就是作用范围
"""

def testA():
    # 在testA函数中num是局部变量
    num = 100
    print(num)

# 出了函数体，就不能识别局部变量


# 全局变量是函数体内，外都能生效的变量

num2 = 25
def testB():
    print(num2)
print(num2)

testA()
testB()

# global关键字可以在函数内部声明变量为全局变量
a = 20
def testC():
    # 声明global为全局变量
    global a
    a = 10
    print(a)
# 函数体外打印变量a
testC()
print(a)


