#1)Positive or Negative:
'''
n=int(input("Enter a number:"))
if n>0:
    print("Positive")
else:
    print("Negative:")
#2)Even or Odd:
n=int(input("Enter a number:"))
if n %2 == 0:
    print(f"{n}: Even")
else:
    print(f"{n}: Odd")
#3. Divisible by 5
n=int(input("Enter a number:"))
if n %5 == 0:
    print(f"{n}:Divisible by 5 ")
else:
    print(f"{n}:Not divisible by 5")
#4. Divisible by  3 and 7:
n=int(input("Enter a number:"))
if n %3 == 0 and n %7 == 0:
    print(f"{n}:Divisible by both 3 and 7 ")
else:
    print(f"{n}:Not Divisible by both 3 and 7 ")
#5. Check for Leap Year:
year=int(input("enter a year:"))
if year%4==0 and (year%400==0 or year%100!=0):
    print("Leap year:")
else:
    print("not a leap year:")

#6. Check Pass or Fail (Passing marks = 35)
marks=int(input("Enter a number:"))
if marks>=35:
    print("Pass")
else:
    print("Fail")
#7. Check if number is 3-digit
digit=int(input("Enter a number:"))
if digit>99 and digit<1000:
    print(f"{digit}: 3 digit")
else:
    print(f"{digit}: Not a 3 digit")
#8. Check if character is vowel

name=list(map(str,input("enter your name:").split()))
vowel='aeiouAEIOU'
for char in name:
    if char in vowel:
        print(char,"is a vowel")
    else:
        print(char,"is not a vowel")
(or)

n=input("Enter your name:")
vowel='aeiouAEIOU'
if n in vowel:
    print(f"{n} is vowel")
else:
    print(f"{n} is not a vowel")
#9. Check greatest of two numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a > b:
    print(f" {a} is greater:")
else:
    print(f" {b} is greater:")
#10. Check smallest of two numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a < b:
    print(f"{a} is smaller:")
else:
    print(f"{b} is smaller:")
#11. Check if number is zero
n=int(input("Enter a number:"))
if n==0:
    print("Zero")
else:
    print("Not a zero:")'''
#12. Check if number is multiple of 10
n=int(input("Enter a number:"))
if n%10==0:
    print("multiple of 10")
else:
    print("not a multiple of 10")
