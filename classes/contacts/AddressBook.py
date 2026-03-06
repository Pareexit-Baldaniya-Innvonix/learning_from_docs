from classes.contacts.Address import Address


class _AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address("121 Admin Rd.", "Concord", "NH", "03301"),
            2: Address("67 Paperwork Ave", "Manchester", "NH", "03101"),
            3: Address("15 Rose St", "Concord", "NH", "03301", "Apt. B-1"),
            4: Address("39 Sole St.", "Concord", "NH", "03301"),
            5: Address("99 Mountain Rd.", "Concord", "NH", "03301"),
        }


_address_book = _AddressBook()


def get_employee_address(employee_id):
    return _address_book.get_employee_address(employee_id)
