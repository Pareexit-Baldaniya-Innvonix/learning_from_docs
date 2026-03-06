from classes.hr.SalaryEmployee import SalaryEmployee
from classes.hr.HourlyEmployee import HourlyEmployee
from classes.hr.CommissionEmployee import CommissionEmployee
from classes.hr.PayrollSystem import PayrollSystem
from classes.hr.DisgruntledEmployee import DisgruntledEmployee
from classes.hr.EmployeeDatabase import EmployeeDatabase
from classes.hr.ProductivitySystem import ProductivitySystem

from classes.hr.policy.HourlyPolicy import HourlyPolicy

from classes.employee.FactoryWorker import FactoryWorker
from classes.employee.Manager import Manager
from classes.employee.SalesPerson import SalesPerson
from classes.employee.Secretary import Secretary
from classes.employee.TemporarySecretary import TemporarySecretary

from classes.contacts.Address import Address

salary_employee = SalaryEmployee(1, "John Smith", 1500)
hourly_employee = HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = CommissionEmployee(3, "Kevin Bacon", 1000, 250)
disgruntled_employee = DisgruntledEmployee(20000, "Anonymous")

payroll_system = PayrollSystem()
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

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(55)

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
