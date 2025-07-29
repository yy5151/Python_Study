"""
定义一个元组
查询年龄所在的下标位置
查询学生的姓名
删除学生爱好的football
增加爱好：coding到爱好list内
"""

tuple = ("小明",21,["football","music"])
# 查询其年龄所在的下标位置
index = tuple.index(21)
print(f"年龄所在的下标位置是：{index}")
# 查询学生的姓名
name = tuple[0]
print(f"学生的姓名：{name}")
# 删除学生爱好中的football
tuple[2].remove("football")
print(f"删除学生爱好中的football后：{tuple}")
# 增加爱好：coding 到爱好list
tuple[2].append("coding")
print(f"增加爱好后：{tuple}")