# 遞迴
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

n = 10
value = fib(n)
print(n, value)

print(9 // 2)
x = 6/2*(1+2)
print(x)

