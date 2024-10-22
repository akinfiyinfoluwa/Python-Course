class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee): 
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck (self):
        return self.hourly_rate * self.weekly_hours
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, comms_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.coms_rate = comms_rate
    
    def calculate_paycheck(self):
        return super().calculate_paycheck() + (self.sales_num * self.coms_rate)

      
       
        
        