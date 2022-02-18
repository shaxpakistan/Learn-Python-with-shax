value1 = float(input("Enter value1 :"))
value2 = float(input("\nEnter value2 "))

choice = input("\nEnter operation to calculate\n\'+' for addition operation\n\'-' for substraction operation\n\'*' for multiplication operation\n\'/' for division operation\n\t: ")

def add(a, b):
    return a+b

def sub(a,  b):
    if a > b:
        return a - b
    else:
        return b - a
    
def pro(a, b):
    return a*b

def div(a, b):
    if a > b:
        return a / b
    else:
        return b / a
    
if choice == "+":
    print("Summation of ",value1," and ",value2," is :",add(value1,value2))
elif choice == "-":
    print("Difference of ",value1," and ",value2," is :",sub(value1,value2))
elif choice == "*":
    print("Product of ",value1," and ",value2," is :",pro(value1,value2))
elif choice == "div":
    print("Dividion of ",value1," and ",value2," is :",div(value1,value2))
else:
    print("You entered wrong operation...")