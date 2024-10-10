# PRIME NUMBER

def prime_number(number):
    if number <= 1:
        print("THE NUMBER SHOULD BE GREATER THAN 1")
        return

    for i in range(2, number):
        if number % i == 0:
            print("NOT A PRIME NUMBER")
            return
    
    print("PRIME NUMBER")


number = int(input("ENTER THE NUMBER: "))
prime_number(number)