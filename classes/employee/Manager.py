from classes.hr.SalaryEmployee import SalaryEmployee

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")