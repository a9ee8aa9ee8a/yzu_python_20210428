# 數組: list(元素可重複), set(元素不可重複), dict(key/value 組合元素)

scores = [100, 90, 80, 80]   # list
scores.append(70)
print(scores)
print(scores[1])   # 取得維度 = 1 的資料(維度從0開始)
print(len(scores))   # 取得元素個數
print(scores.index(80))   # 取得某元素的維度值(回傳第一個符合的index)
print(max(scores), min(scores))   # 取得元素最大最小值

# 走訪每一個元素
for x in scores:
    print(x)
# 走訪每一個元素(含維度值)
for (idx, values) in enumerate(scores):   # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    print(idx, values)
