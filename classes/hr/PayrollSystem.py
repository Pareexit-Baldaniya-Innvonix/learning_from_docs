from classes.hr.policy.SalaryPolicy import SalaryPolicy
from classes.hr.policy.CommissionPolicy import CommissionPolicy
from classes.hr.policy.HourlyPolicy import HourlyPolicy


class _PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9),
        }


_payroll_system = _PayrollSystem()


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    _payroll_system.calculate_payroll(employees)
