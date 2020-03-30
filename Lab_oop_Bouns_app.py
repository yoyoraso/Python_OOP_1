from Lab_oop import Employee
from Lab_oop_p2 import Manager

print("""
=======================================
=         [Employee MeNU]              =
=         ===============              =
= To Show Employee List -----> show    =
= To Add New Employee Enter -----> add =
=    IF MANAGER Enter ------> m        =
=    To Show Managers -----> show      =
=     Then Enter ---> add              =
= Then Insert Data                     =
----------------------------------------
=     IF Employee Enter -----> e       =
=    To Show Managers -----> show      =
=     Then Enter ---> add              =
= Then Insert Data                     =
=                                      =
= ((IF You Want to QUIT Enter ----> q))=
""")

flag = 0
while flag == 0:
    add = input("-----------> : ")
    if add.lower() == "add":
        add = input("---->")
        if add.lower() == "e":
            add = input("---->")
            if add.lower() == "add":
                fname = input("first name : ")
                lname = input("last name : ")
                age = int(input("age : "))
                depart = input("department : ")
                salary = int(input("salary : "))
                emp = Employee(fname, lname, age, depart, salary)
            elif add.lower() == "show":
                Employee.display()
            # elif add.lower() == "fire":
            #     Employee.emp1.fire()
            # elif add.lower() == "tran":
            #     Employee.emp1.transfer()
            elif add.lower() == "q":
                flag = 1
            else:
                print("wrong Input")
        elif add.lower() == "m":
            add = input("------->")
            if add.lower() == "add":
                fname = input("first name : ")
                lname = input("last name : ")
                age = int(input("age : "))
                depart = input("department : ")
                salary = int(input("salary : "))
                managed_department = input("managed department : ")
                man = Manager(fname, lname, age, depart, salary, managed_department)
            elif add.lower() == "show":
                Manager.display()
            elif add.lower() == "q":
                flag = 1
            else:
                print("wrong Input")
        elif add.lower == "q":
            flag = 1
    elif add.lower() == "show":
        Manager.display()
        Employee.display()
    elif add.lower() == "q":
        flag = 1
    else:
            print("wrong Input")