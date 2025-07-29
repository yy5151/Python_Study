"""
None就是空,是False,return 空时,函数调用者接收到的返回值就是类型空
但None可以用于判断上
"""
def check_age(age):
    # 判断数值
    if age > 18:
        return "SUCCESS"
    # 小于18,返回None则中断判断,函数的返回值为None
    else:
        return None

# 当age的值为17小于18,则返回值为None,result是None
result = check_age(20)
# 又一判断语句,当result值为空则说明是小于18,not None则是True,就能执行判断语句
if not result:
    print("未成年")