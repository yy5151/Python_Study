# 函数的嵌套调用是指一个函数里面又调用了另外一个函数
def fun_b():
    print("---2---")

def fun_a():
    print("---1---")
    fun_b()
    print("---3---")

fun_a()
