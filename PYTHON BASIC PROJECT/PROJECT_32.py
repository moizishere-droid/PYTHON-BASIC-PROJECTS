#  Password Strength Checker - Check the strength of a password based on certain criteria.

list_of_list = [
    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    list(str(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]).capitalize()),
    ["@","#","$","%","^","&","*","!"],
]

password = input("Enter the password: ")
if(len(password)>=8):
    for a in range(len(list_of_list[2])):
        if list_of_list[2][a] in password:
            print("all good")
            break
        else:
            print("passowrd must contain at least one special character")    
else:
    print("password must be greater than or equal to the length of 8")    