from roles import SecretaryRole
from classes.hr.Employee import Employee
from classes.hr.policy.SalaryPolicy import SalaryPolicy


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)
