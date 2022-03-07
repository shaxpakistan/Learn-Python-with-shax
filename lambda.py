def myfunc(n):
  return lambda a : a * n #this is lambda 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))