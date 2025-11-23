def monthdays():
    month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:21,11:30,12:31}
    #Ask user for month
    month=int(input("Enter the month number(1-12):"))
    #Check if month is valid
    if month<1 or month>12:
        print("Invalid month number.Please enter a value between 1 and 12")
    else:
     #Check leap year
     if month==2:
         leap=input("Is it a leap year? (yes/no):")
         if leap=="yes":
            print("February has 29 days")
         else:
            print("February has 28 days")
     else:
         print("Month",month,"has",month_days[month],"days.")
monthdays()
    
                    