def Vowel_and_constants(string):
    list_of_vowels = ['a','e','i','o','u']
    if(len(string)!=0):
        count = 0
        for x in list_of_vowels:
            for y in string:
                if(x==y):
                    count+=1
        constants = len(string) - count            
        print(f" Vowels = {count} , Constants =  {constants}")            

if __name__ == "__main__":
    string = input("ENter th string : ").lower()
    Vowel_and_constants(string)                    