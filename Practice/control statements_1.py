'''#1. Print Numbers from 1 to N (Using for loop)
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(i)
    
#2. Print Even Numbers from 1 to N (Using for loop)
n=int(input("Enter a number:"))
for i in range(2,n+1,2):
    print(i)
    
#3. Sum of Numbers from 1 to N (Using for loop)
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(f"sum of numbers from 1 to {n} is ",sum)

#4. Print Odd Numbers from 1 to N (Using for loop)
n=int(input("Enter a number:"))
for i in range(1,n+1,2):
    print(i)
#5. Find Factorial of a Number (Using for loop)
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
   fact=fact *i
print(fact)

#6. Print Multiplication Table of N (Using for loop)
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")

#7. Check Prime Number (Using for loop):
n=int(input("Enter a number:"))
if n<=1:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")
#8. Sum of Digits of a Number (Using while loop)
n=input("enter the digitd to sum:").split(",")
sum=0
for i in n:
    sum=sum+int(i)
print(sum)

'''


