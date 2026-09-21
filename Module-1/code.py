print("===== EMPLOYEE PAYROLL MANAGEMENT SYSTEM =====")

employee_name = input("Enter employee name: ")

basic_salary = float(input("Enter basic salary: "))
days_present = int(input("Enter number of days present: "))
total_days = int(input("Enter total working days: "))

allowances = float(input("Enter allowances: "))
deductions = float(input("Enter deductions: "))

# Calculate salary based on attendance
attendance_salary = (basic_salary / total_days) * days_present

# Calculate net salary
net_salary = attendance_salary + allowances - deductions

print("\n===== PAYROLL DETAILS =====")
print("Employee Name:", employee_name)
print("Attendance Salary:", round(attendance_salary, 2))
print("Allowances:", allowances)
print("Deductions:", deductions)
print("Net Salary:", round(net_salary, 2))
