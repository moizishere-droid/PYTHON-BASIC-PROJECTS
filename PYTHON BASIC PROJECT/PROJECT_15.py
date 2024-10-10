#  ROCK PAPER SCCISSOR

import random as r


def Game():
    list1 = ["ROCK","PAPER","SCISSOR"]
    computer_answer = r.choice(list1)
    user_answer = input("ENTER THE CHOICE ROCK , PAPER , SCISSOR: ").upper()
    if(computer_answer == user_answer):
        print(f"DRAW , computer choice: {computer_answer} and your choice: {user_answer}")
    elif(computer_answer=="PAPER" and user_answer=="ROCK"):
        print(f"YOU LOSS  , computer choice: {computer_answer} and your choice: {user_answer} ")
    elif(computer_answer=="SCISSOR" and user_answer=="ROCK"):
        print(f"YOU WON , computer choice: {computer_answer} and your choice: {user_answer}")
    elif(computer_answer=="ROCK" and user_answer=="PAPER"):
        print(f"YOU WOn , computer choice: {computer_answer} and your choice: {user_answer}")
    elif(computer_answer=="ROCK" and user_answer=="SCISSOR"):
        print(f"YOU LOSS , computer choice: {computer_answer} and your choice: {user_answer}")
    elif(computer_answer=="SCISSOR" and user_answer=="PAPER"):
        print(f"YOU LOSS , computer choice: {computer_answer} and your choice: {user_answer}")
    elif(computer_answer=="PAPER" and user_answer=="SCISSOR"):
        print(f"YOU WON , computer choice: {computer_answer} and your choice: {user_answer}")
    else:
        print("INVALID")    

if __name__ == "__main__":
    Game()      