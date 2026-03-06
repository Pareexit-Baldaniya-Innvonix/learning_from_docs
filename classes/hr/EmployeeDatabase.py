from .Employee import Employee


class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {"name": "Mary Poppins", "role": "manager"},
            2: {"name": "John Smith", "role": "secretary"},
            3: {"name": "Kevin Bacon", "role": "sales"},
            4: {"name": "Jane Doe", "role": "factory"},
            5: {"name": "Robin Williams", "role": "secretary"},
        }

    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info


employee_database = _EmployeeDatabase()
