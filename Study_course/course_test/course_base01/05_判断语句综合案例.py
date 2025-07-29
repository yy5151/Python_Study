# 定义一个数字(1~10随机产生),通过三次判断来猜出数字
# 判断错误会提示是大了还是小了
import random
num = random.randint(1,10)
n=int(input("请输入第一次猜测数字"))
if n == num:
    print("第一次就猜中")
else:
    if n > num:
        print("猜大了")
    else:
        print("猜小了")
    n = int(input("请输入第二次猜测数字"))
    if n == num:
        print("第二次就猜中")
    else:
        if n > num:
            print("猜大了")
        else:
            print("猜小了")
        n = int(input("请输入第三次猜测数字"))
        if n == num:
            print("第三次猜中")
        else:
            if n > num:
                print("猜大了,三次机会已用完")
            else:
                print("猜小了,三次机会已用完")
