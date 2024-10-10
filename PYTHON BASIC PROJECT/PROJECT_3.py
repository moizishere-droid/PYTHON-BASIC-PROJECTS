# EVEN OR ODD INDENTIFIER

def even_odd(number):
    if(number>=0):    
        if(number%2==0):
            print(f"THE GIVEN NUMBER {number} IS EVEN")
        elif(number%2==1):
            print(f"THE GIVEN NUMBER {number} IS ODD")
        else:
            print("THE GIVEN NUMBER IS INVALID")
    else:
        print("THE NUMBER SHOULD NOT BE A NEGATIVE NUMBER")       

if __name__ == "__main__":
    number = int(input("ENTER THE NUMBER : "))
    even_odd(number)