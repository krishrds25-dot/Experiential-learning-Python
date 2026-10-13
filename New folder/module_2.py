def module2(employees):
    print("\n=== MODULE 2: MULTIPLE EMPLOYEE PAYROLL ===")

    try:
        count = int(input("How many employees do you want to add? "))

        if count <= 0:
            print("Enter at least one employee.")
            return

        for i in range(count):
            print(f"\nEnter details for employee {i + 1}")

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
                print("Invalid details. Employee not added.")
                continue

            employee = {
                "id": len(employees) + 1,
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
        print("Invalid input. Please enter correct numbers.")