#Dictionary.py
dictionary = {}
print(dictionary)
dictionary = dict()

student = {"name": "Pravalika","age": 24,"course": "Computer Science"}
print(student) #{'name': 'Pravalika', 'age': 24, 'course': 'Computer Science'}

#Dictionary Operations:
#Accessing Values:
print(student["name"])    # Output: Pravalika
print(student.get("age")) # Output: 24
#Difference Between dict[key] and dict.get(key):
print(student.get("city","not found")) # Output: not found

#Adding and Updating Items:
student = {"name": "Pravalika", "age": 20}
student["course"] = "Python" # Adding a new key-value pair.
print(student) #{'name': 'Pravalika', 'age': 20, 'course': 'Python'}

student = {"name": "Pravalika", "age": 20}
student["age"] = 21 #Updating existing key
print(student)      #{'name': 'Pravalika', 'age': 21}

#Using update() method to add or update multiple key-value pairs.
student = {"name": "Pravalika", "age": 20}
student.update({"course": "Python", "age": 22}) # This will add "course" and update "age"
print(student)

# Adding nested values in a dictionary:
students = {}

# Adding a nested dictionary
students[1] = {"name": "Pravalika", "marks": 90}
students[2] = {"name": "Santhosh", "marks": 85}
print(students) #{1: {'name': 'Pravalika', 'marks': 90}, 2: {'name': 'Santhosh', 'marks': 85}}

#Removing Items from a Dictionary:
#pop(key) :
student = {"name": "Pravalika", "age": 20, "course": "Python"}
student.pop("age")
print(student) #{'name': 'Pravalika', 'course': 'Python'}
#popitem():
student = {"name": "Pravalika", "age": 20, "course": "Python"}
student.popitem()
print(student) #{'name': 'Pravalika', 'age': 20}
#del Keyword:
student = {"name": "Pravalika", "age": 20, "course": "Python"}
del student["course"]
print(student) #{'name': 'Pravalika', 'age': 20}
# Delete the entire dictionary:
del student
#print(student) # student is no longer available
#clear():
student = {"name": "Pravalika", "age": 20, "course": "Python"}
student.clear()
print(student) #{}

#------sample program-------------
# Original dictionary
student = {"name": "Pravalika", "age": 20, "course": "Python", "marks": 90}
print("Original dictionary:", student)
student.pop("age")                     # 1. Remove a specific key using pop()
print("After pop('age'):", student)    
student.popitem()                      # 2. Remove the last inserted item using popitem()
print("After popitem():", student)
del student["course"]                  # 3. Remove a key using del
print("After del student['course']:", student)
student.clear()                        # 4. Clear all items using clear()
print("After clear():", student)
# 5. Delete the entire dictionary (uncomment to test)
# del student
# print(student)  # This will cause an error because 'student' no longer exists

#Dictionary Built-in Methods:
student = {"name": "Pravalika", "age": 20, "course": "Python", "marks": 90}
print(dict.keys(student))            #dict_keys(['name', 'age', 'course', 'marks'])
print(dict.values(student))          #dict_values(['Pravalika', 20, 'Python', 90])
print(dict.items(student))           #dict_items([('name', 'Pravalika'), ('age', 20), ('course', 'Python'), ('marks', 90)])  

#Dictionary Methods for Adding and Updating Data:
details={"id":101,"batch":"DS-15"}
print(details)                        #{'id': 101, 'batch': 'DS-15'}
student.update({"course":"Datascience"})
print(student)                        #{'name': 'Pravalika', 'age': 20, 'course': 'Python', 'marks': 90}
student.setdefault("adddress","not found")
print(student)                        #{'name': 'Pravalika', 'age': 20, 'course': 'Datascience', 'marks': 90, 'adddress': 'not found'}

#Built-in Functions for Dictionaries:
print(len(student))                  # 5
print(min(student))                  # adddress
print(max(student))                  # name
print(sorted(student))               # ['adddress', 'age', 'course', 'marks', 'name']

# Nested Dictionaries:(A dictionary can contain another dictionary as its value).
students = {
    1: {"name": "Pravalika", "age": 20, "course": "Python"},
    2: {"name": "Santhosh", "age": 22, "course": "SQL"},
    3: {"name": "Teju", "age": 21, "course": "Excel"}
}
print(students)
#Output:
     # {1: {'name': 'Pravalika', 'age': 20, 'course': 'Python'},
     # 2: {'name': 'Santhosh', 'age': 22, 'course': 'SQL'},
     #  3: {'name': 'Teju', 'age': 21, 'course': 'Excel'}}

# Change Teju's course to "Power BI"
students[3]["course"] = "Power BI"
print(students[3]) #{'name': 'Teju', 'age': 21, 'course': 'Power BI'}


  













