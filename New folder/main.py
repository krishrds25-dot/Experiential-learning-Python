from module_1 import module1
from module_2 import module2
from module_3 import module3
from module_4 import module4


# Shared employee records
employees = []


def main():
    while True:
        print("\n========================================")
        print("    EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Basic Payroll Calculation")
        print("2. Multiple Employee Payroll")
        print("3. Employee Search and Payroll Reports")
        print("4. Employee Record Management")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            module1(employees)

        elif choice == "2":
            module2(employees)

        elif choice == "3":
            module3(employees)

        elif choice == "4":
            module4(employees)

        elif choice == "5":
            print("Thank you for using the Payroll Management System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()