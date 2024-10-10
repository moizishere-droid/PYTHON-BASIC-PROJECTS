import random as r

def Password():
    letter = ["a", "b", "c", "d"]
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = ["@", "&", "_", "*"]

    string = ""
    for _ in range(3):  
        string += r.choice(letter)
        string += str(r.choice(number))
        string += r.choice(special)
        
    print(string)

Password()
