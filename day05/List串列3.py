# append, insert, extend
scores = [20, 30, 40]
scores.append(50)
print(scores)
scores.insert(0, 10)
print(scores)
scores.insert(-1, 10)  # 負值為從右方開始
print(scores)
scores.append([70, 75, 79])
print(scores)
print(scores[5][0])   # 多維度取值
# extend 將陣列拆開，只塞入元素
scores.extend([80, 82])
print(scores)
