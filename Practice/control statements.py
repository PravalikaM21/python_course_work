'''1. Print Numbers from 1 to N (Using for loop):

n=int(input("enter a number"))
for i in range(1,n+1):
    print(i)

2. Print Even Numbers from 1 to N (Using for loop):

n=int(input("enter a number"))
for i in range(2,n,2):
    print(i)

3. Sum of Numbers from 1 to N (Using for loop):
    
n=map(int,input("enter list of numbers:").split(","))
sum=0
for i in range(1,n+1):
  print(sum)
   (or)
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum from 1 to", n, "is:", sum)

4. Print Odd Numbers from 1 to N (Using for loop):

n=int(input("enter a number"))
for i in range(1,n+1,2):
    print(i)

5. Find Factorial of a Number (Using for loop):
    
n=int(input("enter a number"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(f'{factorial} is factorial of ',n)

6. Print Multiplication Table of N (Using for loop):
    
n=int(input("enter a number"))
for i in range(1,11):
    print(n ,"x" ,i, "=" , n*i)
7. Check Prime Number (Using for loop)

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

28. Sum of First N Odd Numbers (Using for loop):

n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1,2):
    print(i,end=" ")
    sum=sum+i
    print(sum)
    
25. Print Numbers Divisible by 7 (Using for loop):
    
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i%7==0:
        print(i)
        '''
    
    
