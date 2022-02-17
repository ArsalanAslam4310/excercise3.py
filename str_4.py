def show_employee(name, salary=9000):
    
    return name,salary

name=input("Enter a string")
salary =int(input("Enter a salary"))
employee=show_employee(name,salary)
print(name,salary)