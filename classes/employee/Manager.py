from roles import ManagerRole
from classes.hr.Employee import Employee
from classes.hr.policy.SalaryPolicy import SalaryPolicy


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)
