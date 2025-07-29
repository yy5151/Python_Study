"""
1、掌握布尔类型用于表示:真和假:True,False
2、掌握比较运算符用于计算:真和假
==判断内容是否相等
!=是否不等
>大于
<小于
>=大于等于
<=小于等于
"""
bool_1 = True
bool_2 = False
print(f"bool_1的内容是{bool_1},类型是: {type(bool_1)}")
print(f"bool_2的内容是{bool_2},类型是: {type(bool_2)}")


# 比较运算符
num1 = 10
num2 = 10
print(f"num1 == num2的结果是:{num1 == num2}")
print(f"num1 >= num2的结果是:{num1 >= num2}")

num1 = 10
num2 = 15
print(f"num1 == num2的结果是:{num1 == num2}")

print(f"num1>=num2的结果是:{num1 >= num2}")
print(f"num1!=num2的结果是:{num1 !=num2}")
