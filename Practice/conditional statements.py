'''1)1. Positive or Negative:
    
n=int(input("Enter a number:"))
if n!=0:
      if n>1:
          print("positive")
      else:
          print("negative")
else:
    print("zero")
    

2. Even or Odd:

n=int(input("Enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")

3. Divisible by 5:

n=int(input("Enter a number:"))
if n%5==0:
    print("Divisible by 5")

4. Divisible by 3 and 7:

n=int(input("Enter a number:"))
if n%3==0 and n%7==0:
    print("Divisible by both 3 and 7")
else:
    print("not dividible")
    
   (or)
  
n=int(input("Enter a number:"))
if n%3==0:
    if n%7==0:
        print("Divisible by both 3 and 7")
    else:
        print("not divisible")
else:
    print("Exit")

5. Check for Leap Year:

year=int(input("Enter a year:"))
if (year%400==0 or (year%100!=0 and year%4==0)):
    print("leap year")
else:
    print("non_leap year")
6. Check Pass or Fail (Passing marks = 35)

marks=int(input("Enter your marks:"))
pravaif marks>=35:
    print("pass")
else:
    print("fail")
    
7. Check if number is 3-digit

n=int(input("enter a number:"))
if n>=100 and n<=999:
    print("3 gigit number")
else:
    print("not 3 digit")

char=input("enter the charactes or names").lower()
vowels=['a','e','i','o','u']
if char in vowels:
    print("vowel")
else:
    print("not a vowel")

n1=int(input("Enter n1 value:"))
n2=int(input("Enter n2 value:"))
if n1>n2:
    print(f'{n1} is greater:')
else:
    print(f'{n2} is greater:')
         (or)
n1,n2=list(map(int,input("enter n1 and n2:").split(",")))
if n1>n2:
    print(f'{n1} is greater:')
else:
    print(f'{n2} is greater:')
    
10. Check smallest of two numbers:
n1,n2=map(int,input("enter n1 and n2:").split(","))
if n1<n2:
    print(f'{n1} is smaller:')
else:
    print(f'{n2} is smaller:')
    
11. Check if number is zero:

n=int(input("enter a number"))
if n==0:
    print("zero")
else:
    print("not a zero")
    
12. Check if number is multiple of 10:

n=int(input("enter a number"))
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a Multiple of 10")
    
13. Check if age is eligible to vote (18+):

age=int(input("enter your age:"))
if age>18:
    print("You are eligible for voting:")
else:
    print("You are not eligible for voting:")
    
14. Check if number is between 1 and 100:

n=int(input("enter a number"))
if n>=1 and n<=100:
    print(f"{n} in range")
else:
     print(f"{n} is not in range")

15. Check if number is square of another:

n1,n2=map(int,input("enter a number").split(","))
if n1**2==n2:
    print(f'{n2} is square of {n1}')
else:
    print("not a suare:")
    
16. Check if two strings are equal:

name1=input("enter a string:").lower()
name2=input("enter another string:").lower()
if name1==name2:
    print("same string")
else:
    print("not same")

17. Check if a number is prime (basic logic):
'''
n = int(input("Enter a number: "))

if n > 1 and all(n % i != 0 for i in range(2, n)):
    print("Prime number")
else:
    print("Not a prime number")



