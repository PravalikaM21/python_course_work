#4.Python Operators
#1.Arithmetic operators
'''a=20
b=10
print("Addition(+):",(a+b)) #Addition(+): 30
print("Subtraction(-):",(a-b)) # Subtraction(-): 10
print("Multiplication(+):",(a*b)) #Multiplication(+): 200
print("Division(/):",(a/b)) #Division(/): 2.0
print("Floor Division(//):",(a//b)) #Floor Division(//): 2
print("Modulus(%):",(a%b)) #Modulus(%): 0
print("Exponentiation(**):",(a**b)) #Exponentiation(**): 10240000000000

#2.Comparision Operator
a=20
b=10
print("Equal to(==):",(a==b)) #Equal to(==): False
print("Not Equal to(!=):",(a!=b)) # Not Equal to(!=): True
print("Greater than(>):",(a>b)) #Greater than(>): True
print("Less than(<):",(a<b)) #Less than(<): False
print("Greater than or Equal to(>=):",(a>=b)) #Greater than or Equal to(>=): True
print("Less than or Equal to(<=):",(a<=b)) #Less than or Equal to(<=): False

#3.Assignment operators
a=20
b=10
a = b
print("Assign(=):",a) # Assign(=): 10
a+=b
print("Add & Assign(+=):",a) # Add & Assign(+=): 20
a-=b
print("Subtract & Assign(-=):",a) #Subtract & Assign(-=): 10
a*=b
print("Multiply & Assign(*=):",a) #Multiply & Assign(*=): 100
a/=b
print("Divide & Assign(/=):",a) #Divide & Assign(/=): 10.0
a/=b
print("Floor Divide & Assign(//=):",a) #Floor Divide & Assign(//=): 1.0
a%=b
print("Modulus & Assign(%=):",a) #Modulus & Assign(%=): 1.0
a**=b
print("Exponentiate & Assign(**=):",a) #Exponentiate & Assign(**=): 1.0

#4.Logical operators(AND, OR, NOT)
a=10
b=20
c=10
print(a==c and c==10) #True
print(a==10 and a==b) #False
print(a==c or c==10)# True
print(a==b or b==c) #False
print(not a==10)#False
print(not a==20)#True

#5.Membership Operators(in, not in)
li=[1,2,3,4]
print(li)#[1, 2, 3, 4]
print(3 in li)#True
print(1 in li)#True
print(6 in li)#False
print(8 in li)#False
print(50 not in li)#True
print(6 not in li)#True
print(3 not in li)#False

tu=("prava",3,"sam",["sai","hema"],"dharani",70,90)
print(tu)#('prava', 3, 'sam', ['sai', 'hema'], 'dharani', 70, 90)
print(90 in tu)#True
print("prava" in tu)#True
print("jyo" in tu)#False
print(90 not in tu)#False
print(3 not in tu)#False
print("sai" not in tu)#True

s={"prava","sai","pavan","rani","swetha"}
print(s)#{'rani', 'sai', 'pavan', 'swetha', 'prava'}
print(90 in s) #False
print("prava" in s) #True
print("swetha" in s) #True
print("tarun" in s) #False
print("kira" not in s) #True
print("rani" in s) #True
print(90 not in s) # True

d={"name":"Prava","batch":"Ds-15","course":"DS"}
print(d) #{'name': 'Prava', 'batch': 'Ds-15', 'course': 'DS'}
print("name" in d) #True
print("address" in d) #False
print("id" not in d) #True
print("batch" not in d) #False
'''
#6.Identity Operator(is , is not)
a=[1,2,3,4]
b=[1,2,3,4]
c=10
print(a==b) #True
print(a is b) #False
print(a is not c) #True
a=c
print(a is c ) #True
print(a is not c) #False
print(id(a)) #140709545526472
print((id(b))) #1570889115008
print(id(c)) #140709545526472




