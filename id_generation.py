# Task:-1 Smart Employee ID Generator 🆔


print("Enter Employee name:")
name=input()                            

print("Enter year of joining:")
join_date=input()

print("Enter Department name:")
department=input()


def id_generation():
    emp=""
    date=""
    dept=""
    
    for i in name[0:3]:
        emp+=i.upper()
        
    for j in join_date[-2:]:
        date+=j
        
    for k in department[0:3]:
        dept+=k.upper()
        
    print("The Employee ID is",emp+date+dept)
    
            
id_generation()

