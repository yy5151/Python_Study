"""
股价计算小程序
"""

name = "传播智科"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth = 7

# 计算: 经过growth_days天的增长后,股价达到了多少钱

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日的增长系数是:%f,经过%d天的增长后,股价达到了:%.2f"%(stock_price_daily_growth_factor,growth,stock_price*stock_price_daily_growth_factor**growth))

