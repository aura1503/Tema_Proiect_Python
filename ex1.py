#x=4
#y=10

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count=0
    departament="A01"
    def __init__(self, nume, salary, departament):
        super().__init__(nume, salary)
        self.departament=departament
        Manager.mgr_count +=1
    def display_employee(self):
        print("Salary: ", self.salary)

man1=Manager("Ionescu Ion", 2200, "")
man2=Manager("Popescu Ion", 2500, "")
man3=Manager("Enescu George", 2100, "")

man1.display_employee()
man2.display_employee()
man3.display_employee()

emp1=Employee("Ionescu Ion", 2200)
emp2=Employee("Popescu Ion", 2500)
emp3=Employee("Enescu Vali", 2400)

emp1.display_employee()
emp2.display_employee()
emp3.display_employee()

print(man1.mgr_count)
print(emp1.empCount)