
import statistics as stat
import matplotlib.pyplot as plt        # 畫圖外掛
import matplotlib.font_manager as mpl        # 圖表字形外掛

# 調查有五位同學身高與體重如下;
no = [1, 2, 3, 4, 5]   #座號
h = [172, 168, 164, 170, 176]   # cm
w = [62, 57, 58, 64, 64]   # kg
# 問該學生身高與體重的分散程度哪一個大
# 不同單位的分散程度 需要使用「變異係數」判斷
# 變異係數的定義：CV= Sd/avg ×100%，Sd為標準差， avg 代表算術平均數。 CV的意義是計算標準差相對於算術平均數的百分比。 百分比越大，代表資料越分散。
h_cv = stat.stdev(h)/stat.mean(h)
w_cv = stat.stdev(w)/stat.mean(w)
print('身高的 cv: %.2f %%' % (h_cv * 100))
print('體重的 cv: %.2f %%' % (w_cv * 100))

# 繪圖
font = mpl.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.plot(no, h, marker='o', color=(255/255, 0/255, 0/255))   # X軸、Y軸 設定值點 設定顏色
plt.grid(True)   # 設定格線
plt.title('身高統計表', fontproperties=font)
plt.show()
