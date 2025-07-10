#1. String Input:
full_name = input("Enter your full name: ")
print(full_name)
#output:Enter your full name: Pravalika Muchanthala
#Pravalika Muchanthala

#2. Integer Input:
number = int(input("Enter a number: "))
print(number)
#Enter a number: 5
#5

#3. Float Input:
price = float(input("Enter the price: "))
print(price)
#Enter the product price: 70
#70.0

#4. Input as List (Space-separated):
names = input("Enter employee names:").split()
print(names)
#Enter employee names :joseph abijith pranith
#['joseph', 'abijith', 'pranith']

#5. Input as List (Comma-separated):
fruits=(input("Enter the names of fruits:").split(","))
print(fruits) 
#Enter the names of fruits:Banana,Orange,Mango,Grapes
#['Banana', 'Orange', 'Mango', 'Grapes']

#6. List of Integers:
marks = list(map(int, input("Enter your marks:").split()))
print(marks)
#Enter your marks:50 60 80 90
#[50, 60, 80, 90]

#7. List of Floats:
float_num = list(map(float,input("Enter a sequence of numbers:").split()))
print(float_num)
#Enter a sequence of numbers:8 9 70
#[8.0, 9.0, 70.0]

#8. Tuple Input:
count = tuple(map(int,input("count of sub marks and total_stu:").split()))
print(count)
#count of sub marks and total_stu:5 90 40
#(5, 90, 40)

#9. Set Input:
Ages = set(map(int, input("Enter the students age:").split()))
print(Ages)
#Enter the students age:50 40 30 33 22
#{33, 40, 50, 22, 30}

#10. Dictionary Input using eval():
details = eval(input("Enter your details:"))
print(details)
#Enter your details:{"name":"Pravalika","age":24,} 
#{'name': 'Pravalika', 'age': 24}

#11. Multiple Inputs with Unpacking:
name,age,gender,marks =input("Enter your full information:").split()
print("name:",name)
print("age:",age)
print("gender:",gender)
print("marks:",marks)
'''Enter your full information:Pravalika 24 female 90
name: Pravalika
age: 24
gender: female
marks: 90'''