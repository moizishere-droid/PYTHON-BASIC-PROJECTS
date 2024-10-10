# PALINDROME STRING CHECKER

def palindrome(string):

    if(len(string)<0):
        print("THE STRING IS EMPTY")
        return
    if(len(string)>0):
        if(string[0] == string[len(string)-1]):
            print("THE STRING IS PALINDROME")
        else:
            print("THE STRING IS NOT PALINDROME")

string = input("ENTER THE STRING: ")
palindrome(string)