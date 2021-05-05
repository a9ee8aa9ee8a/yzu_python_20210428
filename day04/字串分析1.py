# 字串分析
str = "she sell sea shell on the sea shore"
print(str)

# 去除左右空白
str = str.strip()
str = str.lstrip() #去除左邊空白
str = str.rstrip() #去除右邊空白
print(str)

print('字串長度:', len(str))
print('有幾個s:', str.count('s'))
print("on這個字的位置", str.find('on'))
print("off這個字的位置", str.find('off'))
print('有沒有sea這個字:', '有' if str.find('sea') >= 0 else '沒有')
print('有沒有land這個字:', '有' if str.find('land') >= 0 else '沒有')
print('此字串有幾個單字:', str.count(' ')+1)

# 是否都是英文字(Aa-Zz)
print("是否都是英文字", str.replace(' ', '').isalpha())   # 利用replace 取代空白,以防止程式判斷錯誤


