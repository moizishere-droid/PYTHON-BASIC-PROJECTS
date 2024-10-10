# FIBONACCI SQUENCE GENERATOR

def fibonaci_squence(numeber):
    if(numeber>0):
        total = 2
        prev = 0
        curr = 1
        add = prev + curr
        print(prev , curr , add , end=" ")
        while(total!=numeber):
            prev = curr
            curr = add
            total+=1
            add = prev + curr
            print(add , end=" ")
    else:
        print("THE NUMBER MUST BE GREATER THAN 0")   

number = int(input("ENTER THE NUMBER: "))
fibonaci_squence(number)         
