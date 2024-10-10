# TEMPERATURE CONVERTOR

def temp_convertor_celsius_to_frah(temp):
    frah = (9/5 * temp) + 32
    print(f"{frah:.2f} in frah")

def temp_convertor_frah_to_celsius(temp):
    cel = (temp - 32) * (5/9)
    print(f"{cel:.2f} in celsius")
    
temp = int(input("Enter the temperature in celsius : "))    
temp_convertor_celsius_to_frah(temp)    
temp = int(input("Enter the temperature in fraah : "))    
temp_convertor_frah_to_celsius(temp)    