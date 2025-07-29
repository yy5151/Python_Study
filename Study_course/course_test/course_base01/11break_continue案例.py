import random
money = 10000
for num in range(1,21):
    great = random.randint(1,10)

    if money > 0:
        if great >= 5:
            money = money-1000
            print(f"向员工{num},发工资1000元,账户余额还剩{money}")
        else:
            print(f"员工{num},绩效分{great},低于5,不发工资,下一位")
            continue
    else:
        print("工资发完了,下个月领取吧")
        break

