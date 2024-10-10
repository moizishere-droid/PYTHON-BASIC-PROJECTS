# WORD COUNTER 

def word_counter(string,word):
    if(len(string)>0):
        count = string.count(word)
        print(f"THE TOTAL OCCURRANE OF THE WORDS IS: {count} ")    
    else:
        print("THE STRING IS EMPTY")


string = input("ENTER THE STRING: ")
word = input("ENTER THE WORDS THAT YOU WANT TO COUNT: ")
word_counter(string,word)