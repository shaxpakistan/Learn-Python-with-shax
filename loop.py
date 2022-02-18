#FOR loop

i=0
sum = 0
subs = 0
mult = 0

userin = input("Enter Operation to peform\'+' or \'-' or \'*' operation :")
for i in range(10):
    print(i)
    sum += i
    subs -= i
    mult *= i
    
if userin == "+":
    print("Summation is :",sum)
    
elif userin == "-":
    print("The different btn is :",subs)

elif userin == "*":
    print("The product of range is :",mult)




