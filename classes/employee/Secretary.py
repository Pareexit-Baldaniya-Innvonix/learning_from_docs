from classes.hr.SalaryEmployee import SalaryEmployee

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")