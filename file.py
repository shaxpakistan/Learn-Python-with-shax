#learn some tips of opening,write, and editing the file

f = open ('myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()


print(firstline)
print(secondline)

f.close()

'''
r mode for read only
w mode for writing only
a mode for appending only

r+ mode for both writing and reading 

'''

a = open("myfile.txt", "r")

for line in a:
    print(line, end = '')
    
a.close()

b = open('myfile.txt', 'w')

b.write("\n Python is Funny")
b.write("\n Lets chase it")


b.close()