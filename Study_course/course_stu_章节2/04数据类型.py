"""
数据类型有很多种
当前接触的有:字符型,整型,浮点型

type()语句可查看类型信息
"""
# 定义一个字符型变量,并输出该变量的数据类型信息
s="这是一个字符型变量"
print(s,type(s))

# 定义一个整型变量,并输出该变量的数据类型信息
i=666
print(i,type(i))

# 定义一个浮点型变量,并输出该变量的数据类型信息
f=13.14
print(f,type(f))

# 用一个变量去接收type()返回的结果
s_type=type("字符型")
i_type=type(666)
f_type=type(13.14)
print(s_type,i_type,f_type)