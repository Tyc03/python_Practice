name = "传智播客"
stock_price = 19.99
stock_growthfactor = 1.23
gorwday = 7
stock_code = "003032"
fin_price = stock_price*stock_growthfactor**(gorwday)
print(f"公司：{name},股票代码：{stock_code},当前价格：{stock_price}")
print("每日增长系数是：%.1f" % (stock_growthfactor),"经过 %d的增长后" % (gorwday),"股价达到了：%.2f" % (stock_price*stock_growthfactor**gorwday))
print("每日增长体系：%.1f,经过%d天的增长，开盘价约为:%.2f,收盘价最终为:%.2f" % (stock_growthfactor,gorwday,stock_price*stock_growthfactor**(gorwday-1)
                                                       ,stock_price*stock_growthfactor**gorwday))

