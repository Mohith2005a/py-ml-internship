# Task:-2 Smart Password Validator

print("ENter id")
id=input()

print("Enter password:")
password=input()

pass_len=len(password)

def verify_Password():
    
    caps=0
    digit=0
    spe_char=0
    
    for i in password:
        
        if 'A'<=i<='Z':
            caps+=1
            
        if i.isdigit():
            digit+=1
            
        if not i.isalnum():
            spe_char+=1

            
    if len(password)<8:
        print("Password must me >= 8 characters")
        
    if caps>=1 and digit>=1 and spe_char>=1 :
        pass
    else :
        print("Invalid password")
        
    print("First 3 letters",id[0:3])
    print("Last 3 letters",id[-3:])


verify_Password()
