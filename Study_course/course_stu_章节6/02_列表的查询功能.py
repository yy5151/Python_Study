"""
将函数定义为class类的成员，那么函数会称之为：方法
class 方法名
"""
# class Student:
#     def add(self,x,y):
#         return x+y
#
#
# student = Student()
# num = student.add(1,2)
# print(num)
#
l_list = [5,6,7,8]
# index方法会输出元素在列表的下标，没有就报错
index = l_list.index(8)
print(index)
#
# 修改特定下标索引的值
l_list[0] = "传智教育"
print(l_list)

# 在指定位置插入元素
# 列表.insert(下标，元素)，在指定的下标位置，插入指定元素
my_list = [1,2,3]
my_list.insert(1,"itheima")
print(my_list)
#
# 在列表的尾部追加‘‘‘单个’’’新元素
my_list.append("黑马程序员")
print(my_list)

# 在列表的尾部追加‘‘‘一批’’’新元素
my_list = ["itheima","itcast","python"]
mylist = [1,2,3]
my_list.extend(mylist)
print(my_list)


# 删除指定下标索引的元素（2种方式）
# 方式1：del 列表[下标]
del mylist[2]# 删除下标为2 的元素即3
print(mylist)
# 方式2：列表.pop(下标)
element = my_list.pop(2)# 将元素取出，用element接收
print(element,my_list)

# 删除某元素在列表中的第一个匹配项
mylist = ["itcast","itheima","itcast","itheima","python"]
mylist.remove("itheima")# 删除列表第一个itheima,一次只能删一个
print(mylist)

# 清空列表
mylist.clear()
print(mylist)

# 统计某元素在列表内的数量
my_list = [1,1,1,2,3]
print(my_list.count(1))# 统计元素“1”，在列表内的数量

# 统计列表中全部的元素数量
newlist = [1,2,3,4,5,6,7,8]
count = len(newlist)
print(count)