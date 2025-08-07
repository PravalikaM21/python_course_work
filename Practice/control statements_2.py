'''
s="Programming Language"
print(s)
print(ord("P"))
print(ord("r"))
print(ord("o"))
print(ord("g"))
# 1) Find Order of each character in a given string:
s="Programming Language"
for i in s:
    print(i, ord(i),sep="-", end=" ")
    
# Find squares of give string:
l=[1,2,3,4,5,6]
for num in l:
    print(num, num**2)

# Print Each each string in a given tuple in upper case:
names = ("Prava", "shialu" ,"siri","mouni")
for name in names:
    print(name, name.upper(),sep="-")
    
#Print keys and values in a dictionary:
s={1:1,2:4,3:9,4:16,5:25}
for i in s:
    print(i,s[i])
#Range :
for i in range(10):
    print(i, end=" ")
    
for i in range(1,21):
    print(i, end=" ")
    
for i in range(1,21,2):
    print(i,end=" ")

n=int(input("Enter a table"))
for i in range(1,21):
      print(f"{n}*{i}={n*i}")
    
names = "Prava shialu siri mouni"
for name in names:
    print(name,names.index(name))
  '''
products=['cycle','watch','laptop','mobile','mouse']
item=input("enter an item")
for item in products:
    print(products[item])


































