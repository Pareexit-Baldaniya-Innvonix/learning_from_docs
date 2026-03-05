from .roles import FactoryRole
from classes.hr.Employee import Employee
from classes.hr.policy.HourlyPolicy import HourlyPolicy

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
        super().__init__(id, name)