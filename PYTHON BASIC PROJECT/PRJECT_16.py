# LEAP YEAR CHECKER
# no divided by 100 but divided by 400 --> leap years

def Leap_Year_Checker(year):
    if(year%400==0):
        print("A LEAP YEARS")
    elif(year%4==0  and  year%100!=0):   
        print("A LEAP YEARS")
    else:
        print("Not a leap year")

if __name__ == "__main__":
    year =int(input("Enter the year: "))
    Leap_Year_Checker(year)        