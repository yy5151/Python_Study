import random
num = random.randint(1,10)

# 用于计数循环次数的变量
i=1

# 用于当判断语句满足条件时跳出循环语句
res=True

while res:
    print(f"第{i}次猜")
    n = int(input("请输入一个数字"))
    if n == num:
        print("猜中了")
        # 猜中了就跳出循环
        res=False
    else:
        # 没猜中就把循环次数加1
        i+=1
        if n < num:
            print("猜小了")
        else:
            print("猜大了")
print(f"总共猜了{i}次")
