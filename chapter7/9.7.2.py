import random


class Employee:
    def __init__(self, idx, level):
        assert level in ("respondent", "manager", "director")
        self.id = idx
        self.level = level
        self.able = True

    def take_call(self):
        self.able = False

    def kill_call(self):
        self.able = True


num_employees = 10
levels = ["respondent", "manager", "director"]
employees = []
for index in range(num_employees):
    random.shuffle(levels)
    employees.append(Employee(index, level=levels[0]))
levels = ["respondent", "manager", "director"]

for calls in range(10):
    for level in levels:
        take_call = [
            employee
            for employee in employees
            if employee.level == level and employee.able
        ]
        if take_call:
            take_call[0].take_call()
            print(
                "final status",
                [(employee.able, employee.level) for employee in employees],
            )
            break
