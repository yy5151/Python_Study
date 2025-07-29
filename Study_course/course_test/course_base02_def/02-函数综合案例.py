money = 5000000
def check_money():
    print(f"您当前的余额为:{money}元")
def money_add():
    global money
    money_num = int(input("请输入您要存入的数额"))
    money += money_num
    print("操作成功")
    print(f"您当前余额为:{money}")
def money_decrese():
    global money
    while True:
        money_num = int(input("请输入您要取出的金额数"))
        money -= money_num
        if money <= 0:
            print("您当前余额不足,请重新输入金额数")
            money += money_num
            continue
        else:
            print("操作成功")
            break
    print(f"您当前余额为:{money}")
def case():
    global name
    name = input("请输入您的姓名")
    while True:
        print("请选择您要进行的操作")
        print("1-查询余额,2-存款,3-取款,4-退出")
        check_num = int(input("请输入操作对应的序号数"))
        if check_num == 1:
            check_money()
            print("操作完成!")
            print("----------")
            continue
        elif check_num == 2:
            money_add()
            print("操作完成!")
            print("----------")
            continue
        elif check_num == 3:
            money_decrese()
            print("操作完成!")
            print("----------")
            continue
        else:
            print("当前正在退出")
            break
case()


