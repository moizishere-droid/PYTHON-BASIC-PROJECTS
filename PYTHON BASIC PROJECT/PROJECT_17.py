# INTEREST CALCULATOR 

def Interest_Calculator(inital_amount , interest_yearly , time):
    if(inital_amount<=0 and interest_yearly<=0 and time<=0):
        print("GIVEN DETAIL ARE IN ZERO AND NEGATIVE")
    else:
        interest = (inital_amount * interest_yearly * time) / 100   
        print(f" THE FINAL INTEREST IS GIVEN AS: {interest}")

if __name__ == "__main__":
    inital_amount = int(input("Enter the intial amount: "))
    interest_yearly = float(input("Enter the interest percentage: "))
    time = int(input("Enter the time period in year: "))
    Interest_Calculator(inital_amount,interest_yearly,time)        