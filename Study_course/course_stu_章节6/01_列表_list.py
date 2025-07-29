"""
字面量
[元素1，元素2，元素3，......]

定义变量
变量名称 = [元素1，元素2，元素3，......]

定义空格列表
变量名称 = []
变量名称 = list()
"""

name = ['yuany','puyhon','itcast']
print(name)
print(type(name))
l = [[1,2,3],[4,5,6]]
print(l)

# 列表下标索引，正向索引从0开始
print(name[0])# 结果：yuany
print(name[1])# 结果： puyhon
print(name[2])# 结果：itcast

# 反向索引从-1开始
print(name[-1])# 结果：itcast
print(name[-2])# 结果：puyhon
print(name[-3])# 结果：yuany

# 取出嵌套列表的元素
# 列表从0开始排，1是第2个列表的索引，后一个1是第二个从0下标的第二位
print(l[1][1])# 结果是5
