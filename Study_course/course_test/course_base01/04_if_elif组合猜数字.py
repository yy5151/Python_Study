# 通过if elif组合猜中数字
n=10

if int(input("请猜一个数字:")) == n:
    print("第一次猜就猜中了")
elif int(input("猜错了,第二次,再猜一次吧:")) ==n:
    print("猜对了")
elif int(input("猜错了,再猜一次吧:")) == n:
    print("恭喜,最后一次机会猜对了")
else:
    print("很遗憾,一次都没猜中")

