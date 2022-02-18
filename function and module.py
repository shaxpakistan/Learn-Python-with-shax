def fun1():
    print("This is python friends!")
    
fun1()

print("\n\n\n")
print("Finding the number")

def number(n):
    if n%2 == 0:
        print(n,"\t is even number")
    elif n%3 == 0:
        print(n,"\t is an odd number")
    else:
        print(n,"\t is prime number")
    
number(10)
number(7)
number(2)
number(13)
number(100)
number(11)
number(10.2)


print("\n\n\n")
import prime

a = prime.checkIfprime(13)