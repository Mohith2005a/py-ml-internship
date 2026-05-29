        #Email Verification
print("Enter email address:")
mail=input()

def Verify_Email():
    
    count_at_the_rate=0
    count_dot=0
    
    for i in mail:
        if i=='@':
            count_at_the_rate+=1
        if i=='.':
            count_dot+=1
    if count_at_the_rate != 1 or count_dot == 0:
        print("Enter valid email address")
        return

        
    username,domain=mail.split("@")

    
    for valid_user in username:
        if 'a' <= valid_user <='z' or  valid_user=='-' or valid_user=='_' or valid_user.isdigit():
            pass
        else :
            print("Invalid Email")
            break

        
    vdomain=mail.split('.')[-1]

    
    if vdomain=='com' or vdomain=='in' or vdomain=='org':
            pass
    else :
        print('Invalid Email address')
        return

                
Verify_Email()             


        #Password Verification
print("Enter password:")
password=input()


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


verify_Password()


print("The Email & Password Verification completed")

        
        
