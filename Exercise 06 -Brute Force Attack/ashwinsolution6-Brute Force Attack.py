correct_password="12345"
attempts=5 
#Setting limit to password entries
while attempts>0:
    password=input("Enter the password:")
    if password==correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts-=1 
        if attempts>0:
            print("Incorrect Password")
            print("You have",attempts,"attempts remaining")
        else:
            print("Maximum attempts reached.")