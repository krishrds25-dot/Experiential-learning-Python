def calculate_salary(employee):
    attendance_salary = (
        employee["basic_salary"]
        * employee["days_present"]
        / employee["total_days"]
    )

    return (
        attendance_salary
        + employee["allowances"]
        - employee["deductions"]
    )


def display_employee(employee):
    print("\n------------------------------")
    print("Employee ID:", employee["id"])
    print("Employee Name:", employee["name"])
    print("Basic Salary:", employee["basic_salary"])
    print("Days Present:", employee["days_present"])
    print("Allowances:", employee["allowances"])
    print("Deductions:", employee["deductions"])
    print(f"Net Salary: Rs. {calculate_salary(employee):.2f}")
    print("------------------------------")


def module3(employees):
    print("\n=== MODULE 3: SEARCH AND PAYROLL REPORTS ===")

    while True:
        print("\n1. Search Employee by ID")
        print("2. Search Employee by Name")
        print("3. Display All Employees")
        print("4. Payroll Summary")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                employee_id = int(input("Enter employee ID: "))

                found = False

                for employee in employees:
                    if employee["id"] == employee_id:
                        display_employee(employee)
                        found = True

                if not found:
                    print("Employee not found.")

            except ValueError:
                print("Enter a valid employee ID.")

        elif choice == "2":
            name = input("Enter employee name: ").strip().lower()

            matches = [
                employee for employee in employees
                if name in employee["name"].lower()
            ]

            if matches:
                for employee in matches:
                    display_employee(employee)
            else:
                print("Employee not found.")

        elif choice == "3":
            if not employees:
                print("No employee records available.")
            else:
                for employee in employees:
                    display_employee(employee)

        elif choice == "4":
            total_payroll = sum(
                calculate_salary(employee)
                for employee in employees
            )

            print("\n----- PAYROLL SUMMARY -----")
            print("Total Employees:", len(employees))
            print(f"Total Payroll: Rs. {total_payroll:.2f}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")