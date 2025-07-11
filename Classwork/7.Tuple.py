#PythonTuple.py:
t=tuple()
t=()
t=(1,2,3,4,5,6,7) 
print(t) #(1, 2, 3, 4, 5, 6, 7)
my_tuple=("prava","sneha","siri")
print(my_tuple) #
tup=(1,1.0,"prava",True,(1,2,3),["siri",9,10],{3,4,5},{1:"siri",2:"sam"})
print(tup)
print(len(tup))
fruits = ("apple", "banana", "cherry")
print(fruits)#('apple', 'banana', 'cherry')
colors = ("red", "green", "blue")
print(colors[0]) #red # First element
print(colors[-1])#blue# Last element
#Tuple Unpacking:
student = ("Pravalika", 90, "A+")
name, marks, grade = student
print(name)#Pravalika
print(marks)#90
print(grade)#A+
#Tuple Methods:
#count
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))  # Count how many times 2 appears
print(numbers.index(4))  # Find index of value 4
#index
names = ("Pravalika", "Teju", "Santhosh")
print(names.index("Santhosh"))  # Output: 2
#Built-in Functions (not methods):
num=[1,2,3,4,5]
print(len((1, 2, 3)))#3
print(min(num))#1
print(max(num))#5
print((sum(num)))#15
print(sorted(num))#[1, 2, 3, 4, 5]
print(tuple([1,2,3]))#(1, 2, 3)