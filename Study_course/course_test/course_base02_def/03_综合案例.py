money = 5000000
print("您好，欢迎使用ATM取款机")
name = input("请输入您的姓名")
def case1():
    global money
    print(f"您好，尊敬的{name}先生,您的余额为：{money} 元")
    print("查询结束")

def case2():
    global money
    money = money + int(input("请输入您想要存入金额"))
    print(f"操作成功,您当前余额为{money}")

def case3():
    global money
    money = money - int(input("请输入您想取出的金额"))
    print(f"操作成功,您当前余额为{money}")
def case():
    print("1-查询余额")
    print("2-存款")
    print("3-取款")
    while True:
        case_num = int(input("请输入您想进行的操作"))
        if case_num == 1:
            case1()
        elif case_num == 2:
            case2()
        elif case_num == 3:
            case3()
        else:
            print("输入数字错误，请重新输入")
            continue
        print("是否还要继续操作？")
        result = input("‘yes’为继续，‘no’为退出")
        if result == 'no':
            break
    print("感谢使用")



case()

