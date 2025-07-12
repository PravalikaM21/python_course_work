#8.Sets.py:
s=set()
s={"pravalika","sravani","hema","shailu","Anu","chandhu"}
print(s) #{'sravani', 'chandhu', 'hema', 'Anu', 'shailu', 'pravalika'}
name="pravalika"
print(name * 3) #pravalikapravalikapravalika
set1={1,2,3,4,5,6,6,7,3,2,4}
print(set1) #{1, 2, 3, 4, 5, 6, 7}
s.add("hyma")
s.add(20)
s.add(10.0)
s.add(2+5j)
s.add((1,2,3,4))
print(s) #{10.0, 'shailu', (1, 2, 3, 4), (2+5j), 'sravani', 20, 'chandhu', 'Anu', 'pravalika', 'hema', 'hyma'}
#s.add({3,2,3}) #TypeError: unhashable type: 'set'
#s.add([10,20,30]) #TypeError: unhashable type: 'list'
#s.add({101:"prava"}) #TypeError: unhashable type: 'dict'
s. remove("shailu")
print(s) #{'pravalika', 10.0, 'Anu', (1, 2, 3, 4), (2+5j), 20, 'hyma', 'chandhu', 'hema', 'sravani'}
s.remove("chandhu")
s.remove((10.0))
s.remove((2+5j))
print(s) #{'sravani', 'hyma', (1, 2, 3, 4), 20, 'pravalika', 'Anu', 'hema'}

#Operations on strings:
names={"kiran","teju","uday","santhosh"}
print(names) #{'kiran', 'uday', 'teju', 'santhosh'}
print(len(names)) #4
print("uday" in names) #True
print("santhosh" in names) #True
print("sam" in names) #False
print("teju" not in  names) #False
set2={8,9,2,3,4}
print(set1) #{1, 2, 3, 4, 5, 6, 7}
print(set2) #{2, 3, 4, 8, 9}
print(set1.union(set2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1 | set2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.intersection(set2)) #{2, 3, 4}
print(set1 & set2) #{2, 3, 4}
print(set1 - set2) #{1, 5, 6, 7}
print(set1.difference(set2)) #{1, 5, 6, 7}
print(set1.symmetric_difference(set2)) #{1, 5, 6, 7, 8, 9}
print(set1 ^ set2) #{1, 5, 6, 7, 8, 9}

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2)) #True
print(set1 <= set2) #True
print(set2.issuperset(set1)) #True
print(set2 >= set1) #True

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) #set1 = {1, 2, 3}

#Built-in Methods:
my_list={"prava","uday"}
print(my_list) #{'prava', 'uday'}
print(len(my_list)) #2
my_list.add("kiran")
print(my_list) #{'kiran', 'prava', 'uday'}
my_list.remove("prava")
print(my_list) #{'kiran', 'uday'}
my_list.discard("uday")
print(my_list) #{'kiran'}
my_list1 = {1,2,3,5,7,3,6,8,9,10}
print(my_list1) #{1, 2, 3, 5, 6, 7, 8, 9, 10}
my_list1.pop()
print(my_list1) #{2, 3, 5, 6, 7, 8, 9, 10}
li1={2,3,4,5}
li1.clear()
print(li1) #set()
print(set1) #{1, 2, 3}
print(set2) #{4, 5, 6}
set1.update(set2)
print(set1) #{1, 2, 3, 4, 5, 6}
set1.intersection_update(set2)
print(set1) #{4, 5, 6}
set1.difference_update(set2)
print(set1) #set()
set1.symmetric_difference_update(set2)
print(set1) #{4, 5, 6}
print(len(set1)) #3
print(max(set1)) #6
print(min(set1)) #4
print(sum(set1)) #15
print(sorted(set1)) #[4, 5, 6]

#Frozensets
frozen = frozenset([1, 2, 3])
print(frozen) #frozenset({1, 2, 3})