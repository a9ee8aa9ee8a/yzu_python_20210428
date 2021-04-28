import  math
'''
    有三組資料:
    170, 50;
    180, 70;
    160, 60;
    計算bmi
'''
def PrintBMI(h, w):
    bmi = w /math.pow((h/100), 2)
    if bmi > 23:
        result = "過重"
    elif bmi < 18:
        result = "過輕"
    else:
        result = "正常"
    print(" h=%.1f w=%.1f bmi=%.2f  %s" % (h, w, bmi, result))

PrintBMI(170, 50)
PrintBMI(180, 70)
PrintBMI(160, 60)
