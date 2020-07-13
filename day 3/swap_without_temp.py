a = int(input("enter the no:"))
b = int(input("enter the no:"))

def swap(a,b):
    a,b = b,a
    return f"after swapping a and b =" ,a,b

print(swap(a,b))