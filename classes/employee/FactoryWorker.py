from classes.hr.HourlyEmployee import HourlyEmployee

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")