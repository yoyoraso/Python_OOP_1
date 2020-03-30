from Lab_oop import Employee


class Manager (Employee):
    man_list = []
    manCount = 0
    def __init__(self,f_name,l_name,age,dep,salary,man):
        Employee.__init__(self,f_name,l_name,age,dep,salary)
        self.man = man
        Manager.emp_list.append (self)
        Manager.manCount += 1
        f = open("Manager.txt", "a")
        for i in [(self.f_name), " ", (self.l_name), "         ", (str(self.age)), "        ", (self.dep), "        Salary **** (Confidentail)        ", (str(self.man))]:
            f.write(i)
        f.write("\n")
        f.close()
    def displayEmployee(self):
        print("Name : ", self.f_name, self.l_name,",Age :", self.age, ",Department :" , self.dep,",Salaty : CONFIDENTIAL",",Department_Managed :" ,self.man)
    def display():
        f = open("Manager.txt", "r")
        lines = f.readlines()
        for line in lines:
            print(line)
        f.close()

man1 = Manager ("ahmed","hu",30,"OTT",30000,"OT")
man1.displayEmployee()