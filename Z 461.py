n = int(input())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __lt__(self, other):
        if self.salary == other.salary:
            return self.name < other.name
        return self.salary < other.salary

employees = []
for i in range(n):
    name, salary = input().split()
    employees.append(Employee(name, int(salary)))

employees.sort()
for employee in employees:
    print(employee.name, employee.salary)
