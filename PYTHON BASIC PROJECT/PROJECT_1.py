#  NUMBER GUESSES GAME
import random as r 
def Guess_Game():
    random_guess = r.randint(1,10)
    chances_complete = 0
    while(chances_complete!=5):
        chances_complete+=1
        user_input = int(input("Enter the number between 1 to 10: "))        
        if(user_input == random_guess):
            print(f" YOU HAVE GUEESS THE CORRECT NUMBER {user_input} in {chances_complete} chances")
            break
        elif(user_input != random_guess):
            print(f" YOU HAVE GUEESS THE WRONG NUMBER {user_input} , TRY AGAIN")
        else:
            print("INVALID INPUT PLEASE TRY AGAIN")
    else:
        print(" YOUR CHANCES TO GUESS IS FINISHED PLEASE TRY AGAIN")
        print(f"THE CORRECT NUMBER WAS {random_guess}")    


if __name__ == "__main__":
    print("              ************LET START THE NUMBER GUESSING GAME*********\n")    
    Guess_Game()
    print("  \n            ************LET START THE NUMBER GUESSING GAME********* ")    