my_dict1 = {"语文":98,"数学":99,"英语":100}
print(f"字典1的内容是：{my_dict1},类型是：{type(my_dict1)}")
my_dict2 = {}
print(f"字典2的内容是：{my_dict2},类型是：{type(my_dict2)}")
my_dict3 = dict()
print(f"字典3的内容是：{my_dict3},类型是：{type(my_dict3)}")

# 字典不允许有重复的键，如果有，后面的键值对会覆盖前一个
my_dict1 = {"语文":98,"语文":99,"英语":100}
print(f"重复key的字典的内容是：{my_dict1}")

# 从字典中基于key获取value
my_dict1 = {"语文":98,"数学":99,"英语":100}
score = my_dict1["英语"]
print(f"获取英语成绩：{score}")


# 字典的嵌套
s_list = {"益海":{"语文":78,"数学":89,"英语":92},
          "桃桃":{"语文":98,"数学":89,"英语":97},
          "艺洋":{"语文":83,"数学":99,"英语":72}}
print(s_list)
score = s_list["艺洋"]
print(score)