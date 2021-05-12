e1 = {'name': 'John', 'salary': 50000}
e2 = {'name': 'Mary', 'salary': 60000}
e3 = {'name': 'Bob', 'salary': 70000}
emps = [e1, e2, e3]
print(len(emps), emps)

# 求總薪資
sum_salary = 0
for s in emps:
    sum_salary = sum_salary + s['salary']
print(sum_salary)

# 求最高薪資
# 預先建立 salary = []
salary = []
for emp in emps:
    salary.append(emp['salary'])
max_salary = max(salary)
print(max_salary)
# 求最小薪資
min_salary = min(salary)
print(min_salary)
