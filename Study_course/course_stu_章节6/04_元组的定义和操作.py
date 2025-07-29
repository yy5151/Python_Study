# 元组定义：定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型
"""
定义元组字面量
(元素,元素,元素,.....元素)
定义元组变量
变量名称 = (元素,元素,......,元素)
定义空元组
变量名称 = ()
变量名称 = tuple()
"""

# 定义元组,可以保存各种类型数据
t1 = (1,"Hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t1的类型是：{type(t2)},内容是：{t2}")
print(f"t1的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元素
t4 = ("hello")
print(f"t4的类型是：{type(t4)},t4的内容是：{t4}")# 类型是string
# 小括号只有一个字符型数据则不是元组
# 括号里再有个逗号则为元组类型
t5 = ("hello",)
print(f"t4的类型是：{type(t5)},t4的内容是：{t5}")

# 元组的嵌套
t6 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t6)},内容是:{t6}")

#下标索引取出内容
num = t6[1][2]
print(f"元组取出的内容是{num}")

# 元组操作：index查找方法
t7 = ("传智教育","黑马程序员","python")
index = t7.index("黑马程序员")
print(f"在元组t7中查找黑马程序员的，下标是：{index}")

# 元组操作：count方法统计元组中某个元素的数量
t8 = ("黑马程序员","itheima","itheima","itheima","传智教育")
count = t8.count("itheima")
print(f"在元组t8中itheima元素有{count}个")

# 元组操作：len函数统计元组所有元素的数量
t9 = ("黑马程序员","itheima","itheima","itheima","传智教育","python")
num = len(t9)
print(f"在元组t9中共有{num}个元素")


"""
元组的遍历：while循环，for循环
"""
# 定义一个元组
tuple = ("黑马程序员","itheima","itheima","itheima","传智教育","python")
# 定义下标索引
index = 0
# while循环遍历元组
while index < len(tuple):
    element = tuple[index]# 定义一个变量接收元组元素
    print(element)
    index += 1
print()
# for 循环遍历元组
for element in tuple:
    print(element)
# 可以修改元组里的list的内容（修改元素，增加，删除）
t = (1,2,["itheima","itcast"])
print(f"t的内容是：{t}")
# 修改元组中的数组
t[2][0] = "黑马程序员"
print(f"修改后的元组t的内容是：{t}")

