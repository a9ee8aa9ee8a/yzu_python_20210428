import random as r
scores = [100, -10, -20, 90, -80, 999]
# error_scores = scores.pop(1)   # pop 將值從陣列取出 並傳出值 pop() 預設為最後一個
# print(error_scores, scores)
# error_scores = scores.pop(3)
# print(error_scores, scores)

# Teacher_Ans
# error_scores = []
# for s in scores:
#     if s < 0 or s > 100:
#         error_scores.append(s)
# print(scores)
# print(error_scores)
#
# for x in error_scores:
#     scores.pop(scores.index(x))
#
# print(scores)

# 利用pop將不合法的分數撈出 self_Ans
old_scores = []
for a in scores:
    old_scores.append(a)

print(old_scores)
for x in old_scores:
    if x > 100:
        scores.pop(scores.index(x))
    elif x < 0:
        scores.pop(scores.index(x))
print(scores)

# 反轉
scores = [1, 7, 3, 5]
scores.reverse()
print(scores)

# 排序
scores.sort()
print(scores)

# 洗牌( 隨機亂數)
r.shuffle(scores)  # shuffle() 方法将序列的所有元素随机排序。 ! shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
print(scores)

