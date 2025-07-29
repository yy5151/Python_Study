my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
two_new_list = []
"""
遍历列表，取出列表内的偶数，并存入一个新的列表对象中
使用while循环和for循环各操作一次

"""
def while_list():
    index = 0
    while index < len(my_list):
        if index % 2 != 0:
            new_list.append(my_list[index])
        index += 1
    print(f"通过while循环,从列表：{my_list}中取出偶数，组成新列表：{new_list}")
while_list()


def for_list():
    for element in my_list:
        if element % 2 == 0:
            two_new_list.append(element)
    print(f"通过for循环,从列表：{my_list}中取出偶数，组成新列表：{two_new_list}")
for_list()