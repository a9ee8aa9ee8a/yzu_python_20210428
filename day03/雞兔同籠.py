def getChk(y):
    if 2 * (83 - y)+ 4 *y ==240:
        return y
    else:
        return getChk(y+1)
Chk = getChk(0)
Rabbit = 83-Chk
print(Chk, Rabbit)

# 老師解法
def getChkAndRabbit(sum,feet):
    '''
    :param sum: 83
    :param feet: 240
    :return: chk,rabbit
    '''
    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2)/2
        chk = sum - rabbit
        return rabbit, chk
    else:
        print("無法計算")
        return 0, 0

