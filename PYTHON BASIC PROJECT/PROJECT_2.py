# BASIC CALCULATOR IN PYTHON

def CALCULATOR():
    text = "yes"
    while(text!='NO'):
        if(text=="yes"):
            first_number = int(input("ENTER THE FIRST NUMBER: "))
            second_number = int(input("ENTER THE SECOND NUMBER: "))
            operator = (input("ENTER THE OPERATOR: "))

            if(operator=="+"):
                print(f"THE ADDITION OF {first_number} and {second_number} is {first_number+second_number}")
            elif(operator=="-"):    
                print(f"THE SUBTRACTION OF {first_number} and {second_number} is {first_number-second_number}")
            elif(operator=="*"):    
                print(f"THE MULTIPLICATION OF {first_number} and {second_number} is {first_number*second_number}")
            elif(operator=="/"):    
                print(f"THE DIVISION OF {first_number} and {second_number} is {first_number/second_number}")
            elif(operator=="%"):    
                print(f"THE MODULES OF {first_number} and {second_number} is {first_number%second_number}")
            elif(operator=="**"):    
                print(f"THE EXPONENT OF {first_number} and {second_number} is {first_number**second_number}")
            elif(operator=="//"):    
                print(f"THE FLOOR OF {first_number} and {second_number} is {first_number//second_number}")
            else:
                print("INVALID OPERATOR < PLEASE TRY AGAIN") 
            text = input("DO YOU WANT TO CONTINOUE press yes/no: ".lower()) 
        else:
            break    

if __name__ == "__main__":
    CALCULATOR()
