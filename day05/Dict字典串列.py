# dict 是 key : value 的組合數組
salary = {'john': 50000, 'Mary': 60000}
print(salary)   # 字典格式
print('John 的薪資:', salary['john'])
for key in salary:
    print('%s 的薪資 %d' % (key, salary[key]))

# dict 新增元素
salary.setdefault('Bob', 70000)
print(salary)

# 求薪資的總和
sum_salary = 0
for key in salary:
    sum_salary = sum_salary+salary[key]

print('所有員工的薪資總和: %d' % sum_salary)
