#Control_statements.py:
'''
1)for: used to iterate the items. 
       used when we know thw number of iterations.
2)while: used to iterate the items until the specific condition is met. 
         used when we dont know thw number of iterations.
'''
#1)Print the tables:
num = int(input("Enter the table number:"))
for i in range(1,21):
    print(f'{num} * {i} = {num*i}')
#Output:
# Enter the table number:17
17 * 1 = 17
17 * 2 = 34
17 * 3 = 51
17 * 4 = 68
17 * 5 = 85
17 * 6 = 102
17 * 7 = 119
17 * 8 = 136
17 * 9 = 153
17 * 10 = 170
17 * 11 = 187
17 * 12 = 204
17 * 13 = 221
17 * 14 = 238
17 * 15 = 255
17 * 16 = 272
17 * 17 = 289
17 * 18 = 306
17 * 19 = 323
17 * 20 = 340

#2)Print the index of given string:

s='Praveen Harshith varun sheshu krishna'.lower()
n=len(s)
print(n)
ch = input("Enter the char:").lower()
for i in range(n):
    if s[i] == ch:
        print(ch,i)
#Output:
#Enter the char:i
#i 13
#i 32

# 3)Check whether the prosuct is available or not and print the index of products:

products = ['cycle','mobile','laptop','mouse','watch']
items = input("Enter the items:").split()
for i in items:
    if i in products:
        print(products.index(i),i)
    else:
        print(f'{i} is not available')
#Output:
# Enter the items:cycle
#0 cycle
#Enter the items:tv 
#tv is not available

email,pwd = 'xyzgmail.com','xyz123'
max_attempts=5
while max_attempts > 0:
    useremail = input("Enter the email:")
    password = input("Enter the password")
    if email==useremail and pwd==password:
        print('login successfull')
        break
    else:
        print("Invalid login")
        max_attempts-=1
else:
    print("try after sometime")
#Output:
'''
Enter the email:xsm
Enter the passworddd
Invalid login
Enter the email:sf
Enter the passwordsff
Invalid login
Enter the email:sfc
Enter the passwordsfe
Invalid login
Enter the email:sf
Enter the passwordsew
Invalid login
Enter the email:vd
Enter the passwordxee
Invalid login
try after sometime
'''
#Enter the email:xyzgmail.com
#Enter the passwordxyz123
#login successfull

#Print 1 to 20 numbers:
for i in range(1,21):
    print(i,end=" ")
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
 # Print even numbers upto 20
for i in range(2,20,2):
    print(i)
# Print odd numbers upto 20
for i in range(1,20,2):
    print(i)

# Print prime numbers upto 20:
print("Prime numbers up to 20 are:")
for num in range(2, 21):  # Start from 2, since 1 is not a prime number
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num,end=" ")
#Prime numbers up to 20 are:
#2 3 5 7 11 13 17 19 

num=0
while num<=20:
    print(num,end=" ")
    num+=1
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
num=0
while num<=20:
    num+=1
    print(num,end=" ")
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
    
num = 1
print("Odd numbers up to 20:")
while num <= 20:
    if num % 2 != 0:
        print(num,end=" ")
    num += 1
#Odd numbers up to 20:
#1 3 5 7 9 11 13 15 17 19 
num = 1
print("Even numbers up to 20:")
while num <= 20:
    if num % 2 == 0:
        print(num,end=" ")
    num += 1
#Even numbers up to 20:
#2 4 6 8 10 12 14 16 18 20