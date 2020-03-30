class Employee:
    emp_list = []
    empCount = 0
    ap = ""
    def __init__(self,f_name,l_name,age,dep,salary):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.dep = dep
        self.salary = salary
        Employee.emp_list.append (self)
        Employee.empCount += 1
        f = open ("employee.txt","a")
        for i in [(self.f_name)," ",(self.l_name)," ",(str(self.age))," ",(self.dep)," ",(str(self.salary))]:
            f.write (i)
        f.write("\n")
        f.close()
        # ap = print(self.dep)
    def transfer(self,dep):
        self.dep = dep
        with open("employee.txt", "r") as f:
            lines = f.readlines()
        with open("employee.txt", "w") as f:
            for line in lines:
                if  str(self.f_name)and str(self.l_name) not in line :
                    f.write(line)
        f = open("employee.txt", "a")
        for i in [(self.f_name)," ",(self.l_name)," ",(str(self.age))," ",(self.dep),"  ",(str(self.salary))]:
            f.write (i)
        f.write("\n")
        f.close()
        # o = open("employee.txt", "a")
        # for line in open("employee.txt"):
        #     line = line.replace( ap , self.dep)
        #     o.write(line)
        # o.close()
    def fire(self):
        Employee.emp_list.remove(self)
        with open("employee.txt", "r") as f:
            lines = f.readlines()
        with open("employee.txt", "w") as f:
            for line in lines:
                if  str(self.f_name)and str(self.l_name)  not in line :
                    f.write(line)
    def displayEmployee(self):
        print("Name : ", self.f_name  ,  self.l_name ,", Salary: ", self.salary ,",Age :", self.age,",Department :", self.dep)
    def display():
        f = open("employee.txt", "r")
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()
    def li():
        f = open("employee.txt","r")
        lines = f.readlines()
        for line in lines:
            show(line)
        f.close()


emp1 = Employee("mk nj n","salah",30,"ACC",5000)
#emp2 = Employee("mohamed","salem",33,"IT",2000)
#emp3 = Employee("Yahia","ALi",50,"Law",3000)
emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()
emp1.transfer("OOT")
emp1.displayEmployee()
# emp1.fire()