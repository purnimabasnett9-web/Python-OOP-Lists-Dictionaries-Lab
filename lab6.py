#task 1 Employee Salary System
class EmployeeSalarySystem:
    def __init__(self):
        self.__employees = []

#this method adds a employee to the employeesalarysystem
    def add_employee(self, name, position, salary):
        employee = {
            "name": name,
            "position": position,
            "salary": salary
        }

        self.__employees.append(employee)
        print("Employee added successfully!")

    # Displaying all employees
    def display_employees(self):
        if len(self.__employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for employee in self.__employees:
                print("------------------------")
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])

    # Searching employee by their name
    def search_employee(self, name):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                print("\nEmployee Found:")
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])
                return

        print("Employee not found.")

    # Increase salary
    def increase_salary(self, name, amount):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                employee["salary"] += amount
                print("Salary updated successfully!")
                print("New Salary: ", employee["salary"])
                return

        print("Employee not found.")


# Creating the EmployeeSalarySystem 
system = EmployeeSalarySystem()

# Asking the user how many employees to add to the list
num_employee = int(input("How many employees would you like to add? "))

# Add employees using a loop
for i in range(num_employee):
    print("\nEnter details for Employee {i + 1}")

    name = input("Name: ")
    position = input("Position: ")
    salary = float(input("Salary: "))
    system.add_employee(name, position, salary)

# Display all employees
print("\n--- Employee List ---")
system.display_employees()

# Search for an employee
search_name = input("\nEnter employee name to search: ")
system.search_employee(search_name)

# Increasing the employee salary
employee_name = input("\nEnter employee name for salary increase: ")
increase_amount = float(input("Enter amount to increase salary: "))

system.increase_salary(employee_name, increase_amount)

# Display updated employee records
print("\n--- Updated Employee List ---")
system.display_employees()