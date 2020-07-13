def fahr_to_kelvin(F):
    return 273.5 + ((F - 32.0) * (5.0/9.0)) 

def fahr_to_celcius(F):
    return (F - 32) * 5.0/9.0

F = int(input("Enter the temperature in Fahrenheit:"))
i = int(input(''' Enter the temperature format to convert:
    1,kelvin
    2,celcius 
    >'''

))

if (i == 1):
    print(fahr_to_kelvin(F))

if (i == 2):
    print(fahr_to_celcius(F))

else:
    print("you enter the invalid number. choose the given choice")


