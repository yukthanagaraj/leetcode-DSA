# Definition for Employee.
# class Employee:
#     def __init__(self, id, importance, subordinates):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        emp_map = {}

        for emp in employees:
            emp_map[emp.id] = emp

        def dfs(emp_id):
            employee = emp_map[emp_id]
            total = employee.importance

            for sub_id in employee.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)
        