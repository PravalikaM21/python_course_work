#1)Print the tables:
'''
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
'''
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
'''Enter the email:xsm
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