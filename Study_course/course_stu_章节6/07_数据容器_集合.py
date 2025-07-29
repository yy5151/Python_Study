"""
集合可以去重，并且是无序所以不能下标索引访问，可以修改内容
集合的定义语法：{}
"""
my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty = set() # 定义空集合
print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty},类型是：{type(my_set_empty)}")


# 语法：集合.add(元素)。将指定元素添加到集合内。集合本身被改变
my_set.add("hello")
print(my_set)
# 集合去重的特性会使得添加重复元素不会被重复打印



# 语法：集合.remove(元素)。将指定元素从集合内移除。集合本身被改变
my_set.remove("hello") #移除hello 改变了集合
print(my_set)


# 随机取出一个元素,集合就会没有那个被取出的元素
# 语法：集合.pop()
elempent = my_set.pop() # 列表中的用法是取出指定下标元素
print(f"集合被取出元素是：{elempent},取出元素后集合：{my_set}")


# 清空集合的方法：集合.set()
new_set = {"你好","Python","itheima"}
print(f"清空集合new_set前：{new_set}")
new_set.clear()
print(f"清空集合new_set后：{new_set}")



# 取出2个集合的差集
# 语法：集合1.difference(集合2)。功能：取出集合1和集合2的差集(集合1有而集合2没有的)
# 结果：得到一个新集合，而集合1和集合2不变
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"集合1{set1}")
print(f"集合2{set2}")
print(f"集合3{set3}")





# 消除2个集合的差集
# 语法：集合1.difference_update(集合2)
# 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果：集合1被修改，集合2不变
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"集合1{set1}")
print(f"集合2{set2}")




# 2个集合合并
# 语法：集合1.union(集合2)
# 功能：得到新集合，集合1和集合2不变
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"集合1{set1}")
print(f"集合2{set2}")
print(f"集合3{set3}")



# 统计集合元素数量len()
set1 = {1,2,3,4,5,1,2,3,4,5}
num = len(set1)
print(f"集合内的元素数量有：{num}个")



"""
集合的遍历，集合不支持下标索引，不能用while循环
但可用for循环
"""
set1 = {1,2,3,4,5}
for element in set1:
    print(f"集合的元素有：{element}")





my_list = ["黑马程序员","传智教育","黑马程序员","传智教育","itheima","itcast","itheima","itcast"]
empty_set = set()
for i in my_list:
    empty_set.add(i)
print(f"有列表：{my_list},存入集合后结果：{empty_set}")