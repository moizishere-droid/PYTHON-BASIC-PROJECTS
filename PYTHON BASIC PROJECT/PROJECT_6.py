# FACTORIAL FINDER

def factorial(number):

    if(number==0 or number==1):
        print("THE FACTORIAL OF THE NUMBER IS 1")
        return
    if(number>0):
        total = number-2
        prev = number
        curr = number - 1
        mul = prev * curr 
        while(total!=0):
            prev =mul
            curr = curr-1
            total -=1 
            mul = prev * curr
        print(f"THE FACTORIAL OF THE NUMBER IS {mul}")   
    else:
        print("THE NUMBER SHOULD NOT BE NEGATIVE")       

number = int(input("ENTER THE HUMBER OF WHICH YOU WANT TO FIND FACTORIAL: "))
factorial(number)