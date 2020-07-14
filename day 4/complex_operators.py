def sub_complex(a , b):
     return a - b

def add_complex(a , b):
     return a + b

def mul_complex(a , b):
     return a * b

def div_complex(a , b):
     return a / b

def mod_complex(a , b):
     return a % b     

z1= int((input("enter the real numbers of first complex no:" )))
z2= int((input("enter the imaginary numbers of first complex no:" )))
z3= int((input("enter the real numbers of second complex no:" )))
z4= int((input("enter the imaginary numbers of second complex no:" )))

a = complex(z1, z2)
b = complex(z3, z4)

option = int(input('''>enter the operations to be done.
 1, sub.
 2, add.
 3, mul.
 4, div.
 5, mod.
 '''))

if option == 1:
    print("the result is:",add_complex(a,b))

if (option == 2):
    print("the result is:",sub_complex(a,b))

if (option == 3):
    print("the result is:",mul_complex(a,b))

if (option == 4):
    print("the result is:",div_complex(a,b))

if (option == 5):
    print("the result is:",mod_complex(a,b))

