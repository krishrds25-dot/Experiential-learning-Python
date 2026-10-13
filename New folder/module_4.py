def module4(employees):
    print("\n=== MODULE 4: EMPLOYEE RECORD MANAGEMENT ===")

    while True:
        print("\n1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Display Employees")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                name = input("Employee name: ").strip()
                basic_salary = float(input("Basic salary: "))
                total_days = int(input("Total working days: "))
                days_present = int(input("Days present: "))
                allowances = float(input("Allowances: "))
                deductions = float(input("Deductions: "))

                if (
                    not name
                    or basic_salary < 0
                    or total_days <= 0
                    or days_present < 0
                    or days_present > total_days
                    or allowances < 0
                    or deductions < 0
                ):
                    print("Invalid employee details.")
                    continue

                employee = {
                    "id": max(
                        (e["id"] for e in employees),
                        default=0
                    ) + 1,
                    "name": name,
                    "basic_salary": basic_salary,
                    "total_days": total_days,
                    "days_present": days_present,
                    "allowances": allowances,
                    "deductions": deductions
                }

                employees.append(employee)
                print("Employee added successfully!")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            try:
                employee_id = int(
                    input("Enter employee ID to update: ")
                )

                employee = next(
                    (e for e in employees if e["id"] == employee_id),
                    None
                )

                if employee is None:
                    print("Employee not found.")
                    continue

                name = input(
                    f"New name [{employee['name']}]: "
                ).strip()

                if name:
                    employee["name"] = name

                basic_salary = float(input("New basic salary: "))
                total_days = int(input("New total working days: "))
                days_present = int(input("New days present: "))
                allowances = float(input("New allowances: "))
                deductions = float(input("New deductions: "))

                if (
                    basic_salary < 0
                    or total_days <= 0
                    or days_present < 0
                    or days_present > total_days
                    or allowances < 0
                    or deductions < 0
                ):
                    print("Invalid details. Update cancelled.")
                    continue

                employee["basic_salary"] = basic_salary
                employee["total_days"] = total_days
                employee["days_present"] = days_present
                employee["allowances"] = allowances
                employee["deductions"] = deductions

                print("Employee updated successfully!")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                employee_id = int(
                    input("Enter employee ID to delete: ")
                )

                employee = next(
                    (e for e in employees if e["id"] == employee_id),
                    None
                )

                if employee:
                    employees.remove(employee)
                    print("Employee deleted successfully!")
                else:
                    print("Employee not found.")

            except ValueError:
                print("Enter a valid employee ID.")

        elif choice == "4":
            if not employees:
                print("No employee records available.")
            else:
                for employee in employees:
                    print("\nID:", employee["id"])
                    print("Name:", employee["name"])
                    print("Basic Salary:", employee["basic_salary"])
                    print("Days Present:", employee["days_present"])

        elif choice == "5":
            break

        else:
            print("Invalid choice.")