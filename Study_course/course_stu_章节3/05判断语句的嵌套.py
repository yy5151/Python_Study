"""
if 嵌套使用
"""

# 条件一:大于18岁
# 条件二:小于30岁
# 条件三:要么入职时间大于两年,要么级别大于三
age = int(input("请输入您的年龄:"))
if age >= 18:
    print("第一层判断是否大于18岁")
    if age <= 30:
        print("第二层判断是否小于30岁")
        if int(input("请输入您的入职时间")) >=2:
            print("年龄,入职时间均满足")
        elif int(input("您的入职时间不足2年,请输入您的级别")) >=3:
            print("年龄满足,级别满足")
        else:
            print("只有年龄满足")
    else:
        print("年龄过大")
else:
    print("年龄过小")