from classes.hr.SalaryEmployee import SalaryEmployee
from classes.hr.HourlyEmployee import HourlyEmployee
from classes.hr.CommissionEmployee import CommissionEmployee
from classes.hr.PayrollSystem import _PayrollSystem
from classes.hr.PayrollSystem import calculate_payroll
from classes.hr.DisgruntledEmployee import DisgruntledEmployee
from classes.hr.EmployeeDatabase import _EmployeeDatabase
from classes.hr.ProductivitySystem import _ProductivitySystem
from classes.hr.ProductivitySystem import track
from classes.hr.EmployeeDatabase import _EmployeeDatabase
from classes.hr.policy.HourlyPolicy import HourlyPolicy
from classes.hr.policy.LTDPolicy import LTDPolicy
from classes.hr.Employee import Employee

from classes.employee.FactoryWorker import FactoryWorker
from classes.employee.Manager import Manager
from classes.employee.SalesPerson import SalesPerson
from classes.employee.Secretary import Secretary
from classes.employee.TemporarySecretary import TemporarySecretary

from classes.contacts.Address import Address

import json

salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = CommissionEmployee(3, "Kevin Bacon", 1000, 250)
disgruntled_employee = DisgruntledEmployee(20000, "Anonymous")

payroll_system = _PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee, disgruntled_employee]
)

manager = Manager(1, "Mary Poppins", 3000)
manager.address = Address("121 Admin Rd", "Concord", "NH", "03301")

secretary = Secretary(2, "John Smith", 1500)
secretary.address = Address("67 Paperwork Ave.", "Manchester", "NH", "03101")

sales_guy = SalesPerson(3, "Kevin Bacon", 1000, 250)
factory_worker = FactoryWorker(4, "Jane Doe", 40, 15)
temporary_secretary = TemporarySecretary(5, "Robin Williams", 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]

productivity_system = _ProductivitySystem()
payroll_system = _PayrollSystem()
employee_database = _EmployeeDatabase()

employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(55)

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print("Temporary Secretary:")
print_dict(temp_secretary.to_dict())
