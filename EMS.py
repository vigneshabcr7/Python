# Employee Management System (EMS)

# Step 1: Initialize employee data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anita', 'age': 30, 'department': 'IT', 'salary': 65000}
}

# Step 2: Define functions

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    print("\n--- Add New Employee ---")
    
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id not in employees:
            break
        print("Employee ID already exists. Please enter a unique ID.")

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully!")

def view_employees():
    print("\n--- Employee List ---")

    if not employees:
        print("No employees available.")
        return

    print(f"{'ID':<10}{'Name':<15}{'Age':<10}{'Department':<15}{'Salary':<10}")
    print("-" * 60)

    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<15}{details['age']:<10}{details['department']:<15}{details['salary']:<10}")

def search_employee():
    print("\n--- Search Employee ---")
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Found:")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}")
    else:
        print("Employee not found.")

# Step 6: Run the program
main_menu()
