"""
continue 中断本次循环,直接进入下一次循环
break 直接中断循环,没有循环继续执行
for 循环和while循环效果一样
在嵌套循环中,break 和 continue都只在所在的嵌套循环中生效
"""
# for i in range(1,4):
#     print("语句一")
#     continue
#     # continue跳出本次循环,将不会执行下面的这条语句,但是会把for循环执行完
#     print("语句二")
# print("语句三")
#
# for i in range(1,4):
#     # 只有一次循环被执行了
#     print("语句一")
#     break
#     # break后循环到此结束,不会再执行接下来的语句和循环
#     print("语句二")

# for j in range(1,10):
#     print("语句一")
#     for i in range(1,10):
#         print("语句二")
#         continue
#         # 语句三会被跳出循环后不在被执行
#         print("语句三")
#     print("语句四")

for i in range(1,6):
    print("语句一")
    for j in range(1,6):
        print("语句二")
        break
       # break 后结束内层循环,语句二只被执行一次就结束循环
        # 语句三不会被执行,但循环外的语句不会被影响
        print("语句三")
    print("语句四")