#12.Conditional Statements.py:

#1)if statement:
Age = int(input("Enter your age:"))
if Age > 18:
   print("your eligible for voting:")
if Age < 18:
      print("your not eligible for voting:")
#output:Enter your age:20
      #your eligible for voting:
# 2)If-else:
items=['shoes','smartwatch','phone','laptop','airpods','toycar']
print('Welcome to Amazon store'.center(50,'*'))
searchinput=input("Enter the item:").lower()
if searchinput in items:
    print(f"{searchinput} fouund. Buy now!!!")
else:
    print(f"{searchinput}, is out of stock.we will notify")
#output:Enter the item:shoes
       #shoes fouund. Buy now!!!
#if -elif-else:
#Weekend Budget plan:
amount=int(input("Enter the amount youucan spend for the weekend:"))
if amount>20000:
    print("Trip to Goa")
elif amount>15000:
   print("go for shopping")
elif amount>10000:
   print("clublingg")
elif amount>5000:
   print("cafe/Dinner")
elif amount>2000:
   print("go to movie")
else:
   print("save the money and sleep at home")
#output:Enter the amount youucan spend for the weekend:5000
        #go to movie

#Student marks lists:
students = {1:{"name":"Pravalika","Attempted_exam":"True","Python":90,"SQL":99,"Powerbi":70},
2:{"name":"Teju","Attempted_exam":"false","Python":0,"SQL":0,"Powerbi":0},
3:{"name":"Santhosh","Attempted_exam":"True","Python":80,"SQL":69,"Powerbi":50},
4:{"name":"Anusha","Attempted_exam":"True","Python":50,"SQL":30,"Powerbi":40},
5:{"name":"Hema","Attempted_exam":"True","Python":80,"SQL":50,"Powerbi":78},
6:{"name":"Shivani","Attempted_exam":"True","Python":40,"SQL":35,"Powerbi":40}}
#print(students)
#print(students[1])
#print(students[1]["Attempted_exam"])

students = {
    1: {"name": "Pravalika", "Attempted_exam": "True", "Python": 90, "SQL": 99, "Powerbi": 70},
    2: {"name": "Teju", "Attempted_exam": "false", "Python": 0, "SQL": 0, "Powerbi": 0},
    3: {"name": "Santhosh", "Attempted_exam": "True", "Python": 80, "SQL": 69, "Powerbi": 50},
    4: {"name": "Anusha", "Attempted_exam": "True", "Python": 50, "SQL": 30, "Powerbi": 40},
    5: {"name": "Hema", "Attempted_exam": "True", "Python": 80, "SQL": 50, "Powerbi": 78},
    6: {"name": "Shivani", "Attempted_exam": "True", "Python": 40, "SQL": 35, "Powerbi": 40}
}

if students[1]["Attempted_exam"] == "True":
    total = students[1]["Python"] + students[1]["SQL"] + students[1]["Powerbi"]
    print(f'{students[1]["name"]}, your total marks are: {total}')

if students[2]["Attempted_exam"] == "True":
    total = students[2]["Python"] + students[2]["SQL"] + students[2]["Powerbi"]
    print(f'{students[2]["name"]}, your total marks are: {total}')

if students[3]["Attempted_exam"] == "True":
    total = students[3]["Python"] + students[3]["SQL"] + students[3]["Powerbi"]
    print(f'{students[3]["name"]}, your total marks are: {total}')

if students[4]["Attempted_exam"] == "True":
    total = students[4]["Python"] + students[4]["SQL"] + students[4]["Powerbi"]
    print(f'{students[4]["name"]}, your total marks are: {total}')

if students[5]["Attempted_exam"] == "True":
    total = students[5]["Python"] + students[5]["SQL"] + students[5]["Powerbi"]
    print(f'{students[5]["name"]}, your total marks are: {total}')

if students[6]["Attempted_exam"] == "True":
    total = students[6]["Python"] + students[6]["SQL"] + students[6]["Powerbi"]
    print(f'{students[6]["name"]}, your total marks are: {total}')
#Output:Pravalika, your total marks are: 259
      #Santhosh, your total marks are: 199
      #Anusha, your total marks are: 120
      #Hema, your total marks are: 208
      #Shivani, your total marks are: 115

# write a program to check whether a given number is positive or nagative:
number = int(input("Enter a number:"))
if number > 0:
    print(f'{number} is positive')
else:
    print(f'{number} is negative')
#Output:
        #Enter a number:20
        #20 is positive

# write a program to check whether a given number is even or odd:

number1 = int(input("Enter a number:"))
if number1 > 0:
      print(f'{number1} is positive')
else:
      print(f'{number1} is negative')
#Output:
        #Enter a number:20
        #20 is positive
