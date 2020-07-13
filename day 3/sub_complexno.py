def sub_complex(a , b):
     return a - b

z1= int((input("enter the real numbers of first complex no:" )))
z2= int((input("enter the imaginary numbers of first complex no:" )))
z3= int((input("enter the real numbers of second complex no:" )))
z4= int((input("enter the imaginary numbers of second complex no:" )))

a = complex(z1, z2)
b = complex(z3, z4)

print("The result is:",sub_complex(a,b))
