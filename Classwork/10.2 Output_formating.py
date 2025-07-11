#10.2 Output Formatting.py:
#a) Printing Text:
print("Hello, World!") #Hello, World!
#b) Printing Multiple Items:
name = "Pravalika"
age = 24
print("Name:", name, "Age:", age) #Name: Pravalika Age: 24
#c) Using sep to Change the Separator:
print("2025", "09", "07", sep="-")#2025-09-07
#d) Using end to Control Line Endings:
print("Hello,", end=" ")#Hello, World!
print("World!")
#Printing Special Characters:
print("Pravalika \nMUchanthala")
#Pravalika
#MUchanthala
print("Name:\tPravalika")#Name:   Pravalika
#1️)Using Commas (Simple Print Method):
name = "Pravalika"
age = 24
score = 80
print("Name:", name, "Age:", age, "Score:", score)#Name: Pravalika Age: 24 Score: 80
#2️)Using Modulo Operator (% Formatting):
name = "Santhosh"
age = 29
score = 90
# Using Modulo Operator
print("Name: %s , Age: %d , Score: %f" % (name, age, score))#Name: Santhosh , Age: 29 , Score: 90.000000
#3️)Using f-strings (Formatted String Literals) — Python 3.6+:
name = "Anu"
age = 23
score = 95
# Using f-strings
print(f"Name: {name} , Age: {age} , Score: {score:.2f}")#Name: Anu , Age: 23 , Score: 95.00
#4️)Using str.format() Method:
name = "Teju"
age = 24
score = 75
# Using str.format()
print("Name: {} , Age: {} , Score: {:f}".format(name, age,score))#Name: Teju , Age: 24 , Score: 75.000000
name = "Santhosh"
subject = "Python"
print("Hello {}, welcome to {} class.".format(name, subject))
# Output: Hello Santhosh, welcome to Python class.

print("The {0} is {1} years old.".format("cat", 3))
# Output: The cat is 3 years old.

language = "Python"
version = 3.11
print("We are learning %s version %.2f" % (language, version))
# Output: We are learning Python version 3.11

name = "Pravalika"
marks = 95
print(f"{name} scored {marks} marks.")
# Output: Pravalika scored 95 marks.
