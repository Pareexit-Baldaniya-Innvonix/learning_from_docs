from classes.hr.CommissionEmployee import CommissionEmployee

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")