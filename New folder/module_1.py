def module1(employees):
    print("\n=== MODULE 1: BASIC PAYROLL CALCULATION ===")

    name = input("Enter employee name: ")

    try:
        basic_salary = float(input("Enter basic salary: "))
        total_days = int(input("Enter total working days: "))
        days_present = int(input("Enter days present: "))
        allowances = float(input("Enter allowances: "))
        deductions = float(input("Enter deductions: "))

        if (
            not name.strip()
            or basic_salary < 0
            or total_days <= 0
            or days_present < 0
            or days_present > total_days
            or allowances < 0
            or deductions < 0
        ):
            print("Invalid employee details.")
            return

        attendance_salary = (
            basic_salary * days_present / total_days
        )

        gross_salary = attendance_salary + allowances
        net_salary = gross_salary - deductions

        print("\n----- PAYROLL DETAILS -----")
        print("Employee Name:", name)
        print(f"Basic Salary: Rs. {basic_salary:.2f}")
        print("Days Present:", days_present)
        print(f"Attendance Salary: Rs. {attendance_salary:.2f}")
        print(f"Allowances: Rs. {allowances:.2f}")
        print(f"Deductions: Rs. {deductions:.2f}")
        print(f"Net Salary: Rs. {net_salary:.2f}")

    except ValueError:
        print("Invalid input. Please enter correct numbers.")