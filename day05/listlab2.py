
import statistics as stat
import matplotlib.pyplot as plt        # 畫圖外掛
import matplotlib.font_manager as mpl        # 圖表字形外掛

# 某公司有18位員工，其中10位在去年投資股票，一年的獲
# 利率如下(單位：%)：
#   7.6 3.9 15.6 28.3 1.2 10.8 35.3 45.6 10.2 0.5
# 另外8位員工投資買公債一年內獲利率如下(單位：%)
#   6.8 7.2 6.8 7.5 6.9 7.9 7.9 7.1 7.2
# 試分別求此公司的員工投資股票與公債的獲利率變異係數。
stock = [7.6, 3.9, 15.6, 28.3, 1.2, 10.8, 35.3, 45.6, 10.2, 0.5]
bond = [6.8, 7.2, 6.8, 7.5, 6.9, 7.9, 7.9, 7.1, 7.2]
stock_cv = stat.stdev(stock)/stat.mean(stock)
bond_cv = stat.stdev(bond)/stat.mean(bond)
print('股票變異係數: %.2f %% 公債變異係數 %.2f %%' % (stock_cv, bond_cv))

# 股票、公債 繪圖
font = mpl.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.plot(stock, marker='o', color=(255/255, 0/255, 0/255))   # 股票獲利率線性圖
plt.plot(bond, marker='o', color=(0/255, 0/255, 255/255) )   # 股票獲利率線性圖
plt.ylabel("獲利", fontproperties=font)
plt.grid(True)
plt.title("股票債券獲利表", fontproperties=font)
plt.show()
