import random as r
# 老師解法
ans = r.randint(0,100)
min = 0
max = 100
count = 5   # 限制五次
while True:
    guess = int(input('請輸入 %d ~ %d :' %(min,max)))
    # 檢查 guess 的資料是否在 min 和 max 之間
    if guess <= min or guess >= max:
        print("數字範圍錯誤")
        continue
    # 限制次數
    count = count-1
    # 判定結果
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print("恭喜猜中")
        break
    print("目前剩餘次數: %s" % count)
    if count == 0:
        print("已達限制次數上限，答案為 %s，請重新開始遊戲" % ans)
        break
# 自己解法
# ans = r.randint(0,100)
# min = 0
# max = 100
# while True:
#     guess = int(input('請輸入 %d ~ %d :' %(min,max)))
#     if guess > ans:
#         if max < guess:
#             print("猜太大了")
#             continue
#         else:
#             max = guess
#     elif guess < ans:
#         if min > guess:
#             print("猜太小囉")
#             continue
#         else:
#             min = guess
#     else:
#         print("恭喜猜中")
#         break

