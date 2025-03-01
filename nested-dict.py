company_employees = {}
while True:
    department = input("enter department name or 'stop' to finish: ").strip()
    if department.lower() == "stop":
        break
    
    if department not in company_employees:
        company_employees[department]= {}

    
    employee = input("enter employee name: ").strip()
        

    age = input(f"enter {employee} age: ").strip()
    role = input(f"enter {employee} role: ").strip()

    emp_info= {
        "age":age,
        "role":role,
        }
    
    company_employees[department][employee]=emp_info

print(company_employees)



