from classes.hr.policy.PayrollPolicy import PayrollPolicy


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hourly_rate):
        super().__init__()
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
