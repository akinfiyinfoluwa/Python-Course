from employee import CommissionEmployee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
    
    def pay_employee(self):
        print('Paying customers:')
        for i in self.employees:
          print(f"paycheck for {i.fname} {i.lname}") 
          print(f"The paycheck is ${i.calculate_paycheck():,.2f}")
          print('-----------------')
    
        



def main():
    my_company = Company()

    employee1 = SalaryEmployee('Emma', 'Hess', 50000)
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee('Bayo', 'Olukotan', 20, 100)
    my_company.add_employee(employee2)
     
    employee3 = CommissionEmployee('Bayo', 'Brown', 20000, 5, 2)
    my_company.add_employee(employee3)
      
    my_company.display_employees()
    print('_________')
    my_company.pay_employee()
        

if __name__ == "__main__":
    main()
    


