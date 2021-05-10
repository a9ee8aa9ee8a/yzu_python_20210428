# 印出 2~100 質數
# 質數:一定要兩個因數，且兩個因數只能被自己 跟 1 整除的數

# self-homeworkAns
sted = int(input('請輸入質數範圍開始'))
ended = int(input('請輸入質樹範圍結束'))

def FinalAns(sted, ended):
	result =""
	for i in range(sted, ended):
		chk = 0
		chk = OneAns(i)
		if chk > 0:
			result = result + str(i) +','

	print(result)

def OneAns(numberkey):
	for i in range(2, numberkey):
		if i <= 1:
			return 0
		if numberkey % i == 0:
			return 0
	return 1

FinalAns(sted, ended);
