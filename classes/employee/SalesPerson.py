from roles import SalesRole
from classes.hr.Employee import Employee
from classes.hr.policy.CommissionPolicy import CommissionPolicy


class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)
