from .Secretary import Secretary
from classes.hr.HourlyEmployee import HourlyEmployee

class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hourly_rate)
        
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)