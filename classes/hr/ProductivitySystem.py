from classes.employee.roles.ManagerRole import ManagerRole
from classes.employee.roles.SecretaryRole import SecretaryRole
from classes.employee.roles.SalesRole import SalesRole
from classes.employee.roles.FactoryRole import FactoryRole


class _ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }


_productivity_system = _ProductivitySystem()


def get_role(role_id):
    return _productivity_system.get_role(role_id)


def track(employees, hours):
    _productivity_system.track(employees, hours)
