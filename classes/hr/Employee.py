from representation import AsDictionaryMixin
from classes.contacts.AddressBook import get_employee_address
from .PayrollSystem import get_policy
from .ProductivitySystem import get_role
from .EmployeeDatabase import employee_database


class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get("name")
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get("role"))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy
