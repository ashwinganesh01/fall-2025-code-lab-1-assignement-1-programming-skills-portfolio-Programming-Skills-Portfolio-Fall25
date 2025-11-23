def check_even_odd(number): #Defining the checking even or odd function 
    if number % 2 ==0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

def main():  #Creating a function for asking the user a number and using the check_even_odd function
    num=int(input("Enter a number:"))
    result=check_even_odd(num)
    print(result)
    
#calling main function 
main()