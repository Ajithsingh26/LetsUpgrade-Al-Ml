a = int(input("enter the no:"))
b = int(input("enter the no:"))

def swap(a,b):
    temp = a
    a = b
    b = temp
    return f"after swapping:a = {a} \n b = {b}"

print(swap(a,b))