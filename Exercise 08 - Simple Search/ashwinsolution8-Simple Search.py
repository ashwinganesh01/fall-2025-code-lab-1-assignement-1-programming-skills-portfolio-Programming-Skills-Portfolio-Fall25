Names=["Jake","Zac","Ian","Ron","Sam","Dave"]
search_name="Sam"
if search_name in Names: #Checking if the name "Sam" is in the list
    print("The name",search_name, "found in the list")
ask=input("Enter the name to be searched:") #Asking user for name that should be searched in the list
if ask.capitalize() in Names: #Checking if the name given is present in list
        print("The name",ask,"has been found in the list")
else:
        print("No such name found in the list")

