import random as r
def dice_roller():
    first = r.randint(1,6)
    second = r.randint(1,6)
    print(f"The pair of dice are: {first} and {second} ")

dice_roller()