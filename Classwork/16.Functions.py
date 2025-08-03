# Functions.py
# 1)How do you create a function and call it?
def greet():
    print("Good Mornig")
greet()
#Output:Good Mornig

# 2)How to pass a value to a function?
def greet(name):
    print(f"Hi {name} Good morning")
greet("Pravalika")
'''Output:
Hi Pravalika Good morning'''

#3) How to return a value from a function?
def num(n):
    return n+1
print(num(5)) #6
     #(or)
def add(a,b):
    return a+b
print(add(2,3)) #5
     #(or)
def sub(a,b,c):
    return a-b-c
result=sub(2,3,5)
print(result) #-6
      
# 4)Can we call a function multiple times?(yes):
def add(a,b):
    return a+b
print(add(2,3))     # 5
print(add(5,6))     # 11
print(add(10,20))   # 30
print(add(30,50))   # 80
print(add(100,200)) # 300
        #(or)
def say_hi():
    print("Hi there!")
say_hi()
say_hi()
say_hi()
'''Output:
Hi there!
Hi there!
Hi there!'''

# 5)What happens if a function has no return?
def show():
    print("No return here!")
x = show()
print(x)  #This will print: None
        #(or)
def show():
    print("No return here!")
show()
#Practice:
# Task 1: Greet User Function
def greet_user(name):
    print(f"Hello, {name}! Hava a nice day.")
greet_user("Pravalika")
greet_user("Anu")
greet_user("Santhu")
'''Output:
Hello, Pravalika! Hava a nice day.
Hello, Anu! Hava a nice day.
Hello, Santhu! Hava a nice day.'''
# Task 2: Find Square of a Number:
def square(a):
    return a**2
num=int(input("Enter a number:"))
result=square(num)
print("The square of",num, "is", result)
'''Output:
Enter a number:5
The square of 5 is 25'''
         #(or)
def square(a):
    return a**2
result=square(5)
print(f'The sqauare of 5 is {result}')
'''Output:
The square of 5 is 25'''
        #(or)
def square(a):
    return a**2
num=5
result=square(num)
print(f'The sqauare of {num} is {result}')
'''Output:
The square of 5 is 25'''   
#Task 3: Even or Odd Checker:
def check_even_odd(n):
    if n%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is odd")
num=int(input("enter a number:"))
check_even_odd(num)
'''Output:
enter a number:4
4 is Even='''