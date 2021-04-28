import math

'''
    有三組資料:
    170, 50;
    180, 70;
    160, 60;
    計算bmi
'''


def PrintBmi(h, w):
    bmi = w / math.pow((h / 100), 2)
    # result = "過重" if bmi > 23 else "過重" if bmi <= 18 else "正常"

    # if bmi > 23:
    #     result = "過重"
    # elif bmi < 18:
    #     result = "過輕"
    # else:
    #     result = "正常"   #ctrl + / 快速註解
    result = "過輕"
    if 18 < bmi <= 23:
        result = "正常"
    elif bmi > 23:
        result = "過重"

    print(" h=%.1f w=%.1f bmi=%.2f  %s" % (h, w, bmi, result))


PrintBmi(170, 50)
PrintBmi(180, 70)
PrintBmi(160, 60)
