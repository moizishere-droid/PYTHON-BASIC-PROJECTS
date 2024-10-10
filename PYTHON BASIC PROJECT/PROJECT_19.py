def Currency_Converter(price , country):
    if(price>0):
        match country:
            case 1:
                return (price *( 278.5))
            case 2:
                return (price* (83.25))
            case 3:
                return (price*(0.95))
            case 4:
                return (price*(1.37))
            case _:
                return ("Invalid")
    else:
        print("Enter amounter greater than zero")         

if __name__ == "__main__":
    price = int(input("Enter the price: "))
    dict_1 = {"pakistan":1, "india":2 ,"euro":3,"canada":4}
    country = input("ENter the country : ")
    final = dict_1.get(country)
    result =Currency_Converter(price,final)               
    print(result)