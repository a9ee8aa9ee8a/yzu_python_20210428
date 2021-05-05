import random as r
# 老師解法
ans = r.randint(0,100)
min = 0
max = 100
count = 5   # 限制五次
# 判定結果

def check(guess, who):
    global min, max
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('%s 答對了' % who)
        return True
    return False

while count>0:
    guess = int(input('(%d).請輸入 %d ~ %d :' %(count, min, max)))
    # 檢查 guess 的資料是否在 min 和 max 之間
    if guess <= min or guess >= max:
        print("數字範圍錯誤")
        continue
    # 判定結果
    if check(guess, "me"):
        break

    # 電腦猜
    pc_guess = r.randint(min+1, max-1)
    print("電腦猜數字為 %s" % pc_guess)
    # 判定結果
    if check(pc_guess, "電腦"):
        break;
    # 限制次數
    count = count-1
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

