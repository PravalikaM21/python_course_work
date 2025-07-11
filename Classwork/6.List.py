#6 List.py
l=[1,2,3,4,5,6]
print(l) #[1, 2, 3, 4, 5, 6]
l1=[1,2,3,4,5,6,2,2,44,3,4]
print(l1) #[1, 2, 3, 4, 5, 6, 2, 2, 44, 3, 4]
print(l1[0]) #1
print(l1[4]) #5
print(l1[-1]) #4
print(l1[-5]) #2
print(l) #[1, 2, 3, 4, 5, 6]
l.append("prava")
print(l)
l.extend(["mouna",3,9.0,{3,4,5},(6,7),{101:'sai'},True])
print(l)
l2=["mouna",3,9.0,{3,4,5},(6,7),{101:'sai'},True]
print(l2) #['mouna', 3, 9.0, {3, 4, 5}, (6, 7), {101: 'sai'}, True]
print(l2[3]) #{3, 4, 5}
#Empty List:
list = []
print(list)#[]
#st= list()
#print(lst)#list object is not callable
#List with Elements:
numbers = [1, 2, 3, 4, 5] 
print(numbers)#numbers = [1, 2, 3, 4, 5] 
#List with Nested Lists:
multi_values = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(multi_values)#[[1, 2, 3], ['a', 'b', 'c'], [True, False]]

#3.Accessing Elements in a List:
#Using Indexing (Positive & Negative):
l=[1,2,3,4,5,6]
print(l[1])#2
print(l[0])#1
print(l[3])#4
print(l[-1])#6
print(l[-3])#4
multi_values = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(multi_values[1])#['a', 'b', 'c']
print(multi_values[1][2])#c
print(multi_values[-1])#[True, False]
print(multi_values[-1][0])#True

#Using Slicing:
numbers=[1,2,3,4,5,6]
names=["sam","abhi","Raju","praveen","hyma","pavani","swetha"]
print(numbers[1])#2
print(numbers[::2])#[1, 3, 5]
print(numbers[::])#[1, 2, 3, 4, 5, 6]
print(numbers[-3])#4
print(numbers[-4:])#[3, 4, 5, 6]
print(names[0])#sam
print(names[0::2])#['sam', 'Raju', 'hyma', 'swetha']
print(names[::-1])#['swetha', 'pavani', 'hyma', 'praveen', 'Raju', 'abhi', 'sam']
print(names[-4:-2:-1])#[]
print(names[::-2])#['swetha', 'hyma', 'Raju', 'sam']

#4. Modifying Lists:
#Changing Elements
numbers=[1,2,3,4,5,6]
numbers[0]=2 #[2, 2, 3, 4, 5, 6]
numbers[3]=7#[2, 2, 3, 7, 5, 6]
print(numbers)
#Adding Elements
numbers=[1,2,3,4,5,6]
names=["sam","abhi","Raju","praveen","hyma","pavani","swetha"]
numbers.append(6)
print(numbers) #[1, 2, 3, 4, 5, 6, 6]
numbers.append(8)
print(numbers) #[1, 2, 3, 4, 5, 6, 6,8]
names.append("jyothi")
print(names) #['sam', 'abhi', 'Raju', 'praveen', 'hyma', 'pavani', 'swetha', 'jyothi']
names.extend("Gayathri")
print(names) #['sam', 'abhi', 'Raju', 'praveen', 'hyma', 'pavani', 'swetha', 'jyothi', 'G', 'a', 'y', 'a', 't', 'h', 'r', 'i']
names.extend(["Gayathri","prava","Anu"])
print(names) #['sam', 'abhi', 'Raju', 'praveen', 'hyma', 'pavani', 'swetha', 'jyothi', 'G', 'a', 'y', 'a', 't', 'h', 'r', 'i', 'Gayathri', 'prava', 'Anu']
numbers.extend([1,2,3])
print(numbers)#[1, 2, 3, 4, 5, 6, 6, 8, 1, 2, 3]
numbers.insert(1,1)
print(numbers)#[1, 1, 2, 3, 4, 5, 6, 6, 8, 1, 2, 3]
numbers.insert(1,4)
print(numbers)#[1, 4, 1, 2, 3, 4, 5, 6, 6, 8, 1, 2, 3]
names.insert(0,"mouni")
print(names)#['mouni', 'sam', 'abhi', 'Raju', 'praveen', 'hyma', 'pavani', 'swetha', 'jyothi', 'G', 'a', 'y', 'a', 't', 'h', 'r', 'i', 'Gayathri', 'prava', 'Anu']

#Removing Elements:
numbers=[1,2,3,4,5,6]
names=["sam","abhi","Raju","praveen","hyma","pavani","swetha"]
print(names)
print(numbers.pop())#6
print(numbers.pop(2))#3
print(names.pop())#swetha
print(names.pop(3))#praveen
numbers.remove(5)
print(numbers)#[1, 2, 4]
names.remove("pavani")
print(names)#['sam', 'abhi', 'Raju', 'hyma']
del numbers[2]
print(numbers)#[1, 2]
numbers.clear()
print(numbers)#[] 
num=[1,2,3,4,5,6,2,3]
print(num.index(2)) #1
print(num.index(3)) #2
print(num.index(4)) #3
print(num.count(2)) #2
print(num.count(3)) #2
print(num.count(6)) #1
num.sort()
print(num)#[1, 2, 2, 3, 3, 4, 5, 6]
num.sort(reverse=True)#[1, 2, 2, 3, 3, 4, 5, 6]
print(num)
print(sorted(num))#[1, 2, 2, 3, 3, 4, 5, 6]
print(num)#[6, 5, 4, 3, 3, 2, 2, 1]
num.reverse()
print(num)#[1, 2, 2, 3, 3, 4, 5, 6]
num.copy()
print(num)#[1, 2, 2, 3, 3, 4, 5, 6](shallow copy)
print(min(num))#1
print(max(num))#6
print(len(num))#8
num1=[0,1,2,3,4,5]
print(all(num1))#False
print(any(num1))#True
print(sum(num1))#15
