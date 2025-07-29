"""
常见的转换语句:
int(x)将x转换为一个整数
float(x)将x转换为一个浮点数
str(x)将x转换为字符串
这三个语句都是有返回值,可以用print直接输出
也可以用一个变量存储返回值
"""

# 将数字类型转换为字符串
i=666
print(i,"的类型是",type(i),i)
i_str=str(i)
print("转换后的类型是",type(i_str),i_str)

f=13.14
print(f,"的数据类型是",type(f),f)
f_str=str(f)
print("转换后的数据类型是",type(f_str),f_str)

# 将字符串转换为数字
# 这要求字符串本身就是数字才能转换,文本不能转换
s_1="123"
s_1_int=int(s_1)
print(type(s_1_int),s_1_int)

s_2="12.13"
s_2_float=float(s_2)
print(type(s_2_float),s_2_float)

# 浮点型转整型会将小数点后的数字自动省去
f_2=13.14
f_2_int=int(f_2)
print("f_2:",f_2,type(f_2))
print("转换后:",f_2_int,type(f_2_int))






