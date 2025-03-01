# Company_name = input("enter company name")

company_employees = {}
while True:
    department = input("enter department name or 'stop' to finish: ").strip()
    if department.lower() == "stop":
        break
    
    if department not in company_employees:
        company_employees[department]= {}

    # while True:
    employee = input("enter employee name: ").strip()
        # if employee.lower() == "stop":
        #     break

    age = input(f"enter {employee} age: ").strip()
    role = input(f"enter {employee} role: ").strip()

    emp_info= {
        "age":age,
        "role":role,
        }
    
    company_employees[department][employee]=emp_info

#     # print(emp_info)
#     emp_name={}
#     emp_name[f"{employee}"]= emp_info
    

#     print(emp_name)
#     emp_dep= {}
#     emp_dep[f"{department}"]=emp_name
     
    
#     print(emp_dep)

#     # company_employees={ }
#     company_employees = {
#         "department":emp_dep,
#     }


#     department = input("enter department name: ")

# print(emp_dep)
print(company_employees)

# company_employees={
#     f"{department}" : emp_dep,
# }

# print (company_employees)
# company = {
#     "department1": department
# }

# departments= {
#     "employee":employee
# }

# employees={
#     "age":age,
#     "role": role
# }

# print(employees)
# print(departments)
# print(company)


# company_employees = {
# "Engineering": {
# "Alice": {"age": 30, "role": "Software Engineer"},
# "Bob": {"age": 28, "role": "DevOps Engineer"}
# },
# "HR": {
# "Charlie": {"age": 35, "role": "HR Manager"}
# }
# }

# # print(company_employees)
# # print(company_employees["Engineering"]["Bob"]["role"])
# # print(company_employees["HR"])
# print(company_employees["Engineering"])

# company_employees["Engineering"][f"{employee}"]= employee

# print(company_employees)

