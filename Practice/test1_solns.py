number=int(input("enter a number:"))
if number %2==0:
    print("even winner")
else:
    print("Odd winner")
'''Output:
enter a number:2
even winner
enter a number:9
odd winner'''
#------------------------------------------------------------
st=input("Enter a string")
print(st)
vowels=['a','e','i','o','u']
for i in vowels:
    st=st.replace(i,'*')
print(st)
'''output:
Enter a stringPravalika
Pravalika
Pr*v*l*k*'''
#---------------------------------------------------------------
items=list(map(int,input("Enter item price").split()))
print(items)
total=sum(items)
max_price=max(items)
print(total)
print(max_price)
'''Output:
Enter item price90 70 59 60 49 30 70 122
[90, 70, 59, 60, 49, 30, 70, 122]
550
122'''
#----------------------------------------------------------
username=input("Enter your username")
password=input("Enter your password")
us_na='admin'
pwd='python1223'
if us_na==username:
    if pwd==password:
        print("login successfull")
    else:
        print("Access denied")
else:
    print("acess denied")
'''Output:
Enter your usernameadmin
Enter your passwordpython1223
login successfull
Enter your usernameadmin
Enter your passwordpython
Access denied'''
#-----------------------------------------------------
Bdate=input("Enter your date of birth as 'dd-mm-yyyy':")
print(Bdate)
new_date=Bdate.replace('dd-mm-yyyy','yyyy-mm-dd')
print(new_date)
'''Otput:
Enter your date of birth as 'dd-mm-yyyy':09-08-2007
09-08-2007
09-08-2007'''
#-------------------------------------------------------

names=set(map(str,input("Enter your names").split()))
print(names)
print(sorted(names))
print(names)
'''Output
Enter your namesprava Prava sri sri
{'sri', 'Prava', 'prava'}
['Prava', 'prava', 'sri']
{'sri', 'Prava', 'prava'}'''
#-----------------------------------------------
st=input('enter a string')
print(st)
print(st[-1::-1])
'''Output:
enter a stringhello world
hello world
dlrow olleh'''
#----------------------------------------------------------
di = {}
n = int(input("How many students? "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = input(f"Enter marks of {name}: ")
    di[name] = mark

print("Student Marks Dictionary:")
print(di)
#----------------------------------------------------------

num=list(map(int,input("Enter numbes(separated ny spaces):").split()))
if 0 in num:
    num.remove(0)
    print(num)
else:
    print('p')
'''Output:
Enter numbes(separated ny spaces):90 0 9 4 3 0 20 0 3 0 9
[90, 9, 4, 3, 0, 20, 0, 3, 0, 9]'''
#---------------------------------------------------------'''
num = list(map(int, input("Enter numbers (separated by spaces): ").split()))
while 0 in num:
    num.remove(0)
    print(num)
'''Output:
Enter numbers (separated by spaces): 5 0 0 0 0 9 0 8 0 8 
[5, 0, 0, 0, 9, 0, 8, 0, 8]
[5, 0, 0, 9, 0, 8, 0, 8]
[5, 0, 9, 0, 8, 0, 8]
[5, 9, 0, 8, 0, 8]
[5, 9, 8, 0, 8]
[5, 9, 8, 8]'''
#------------------------------------------------------------------
num = list(map(int, input("Enter numbers (separated by spaces): ").split()))
while 0 in num:
    num.remove(0)
print(num)
'''Output
Enter numbers (separated by spaces): 5 0 0 0 0 9 0 8 0 8
[5, 9, 8, 8]'''
