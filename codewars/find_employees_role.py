def find_employees_role(name):
    employees = [{"first_name": "Dipper", "last_name": "Pines", "role": "Boss"}]
    full_name = name.split()
    
    for emp in employees:

        if (
            emp.get("first_name") == full_name[0]
            and emp.get("last_name") == full_name[1]
        ):
            return emp.get("role")

    return "Does not work here!"


print(find_employees_role("Pines Dipper"))
# print(find_employees_role("Dipper Pines Jones"))
