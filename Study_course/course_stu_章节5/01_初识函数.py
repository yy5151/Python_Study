"""
设计一个函数,用于统计字符串的字符个数
"""
s1 = "mynameissasha"
s2 = "iloveyou"
s3 = "doyouloveme"
# def 声明一个函数
# date 的作用是传参相当于占位,但是参数的占位,并且在接下来的语句中也可用到
def s_len(date):
    count = 0
    for i in date:
        count  += 1
    print(f"字符串{date}的长度是{count}")

# s_len()中的s1,s2,s3就是这个函数的参数
s_len(s1)
s_len(s2)
s_len(s3)
