# List串列與Tuple元組
a = [1, 2, 3, 4, 5]   # 串列 可新增、修改、刪除
b = (1, 2, 3, 4, 5)   # tuple 不可修改  修點:速度快
print(type(a), a)
print(type(b), b)
# 轉換
# List 轉 tuple
a = tuple(a)
print(type(a), a)

# tuple 轉 List
b = list(b)
print(type(b), b)

# remove 移除元素
# 串列能相加
