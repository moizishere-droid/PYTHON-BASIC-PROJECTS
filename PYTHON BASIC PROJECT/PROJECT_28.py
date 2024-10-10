# Simple Email Validator

list_words = ["scam","reward","cash price","transfer","money cashback"]
string = input("enter the string to check: ").casefold()

for word in list_words:
    if word.casefold() in string:
        print("SCAM STRING")
        break
else:
    print("VALID STRING")    