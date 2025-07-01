#3.Python Datatypes
a=10
print(a)#10
a=10.0
print(a)#10.0
print(type(a))#<class 'float'>
a=10
a#10
print(type(a))#<class 'int'>
a=3+3j
a
(3+3j)
print(type(a))
<class 'complex'>
name="pravalika"
print(name)
pravalika
print(type(name))
<class 'str'>
name='pravalika'
print(name)
pravalika
print(type(name))
<class 'str'>
name='''pravalika'''
print(name)
pravalika
print(type(name))
<class 'str'>
fav=[]
fav
[]
print(fav)
[]
print("'tarit' and 'varun'")
'tarit' and 'varun'
print('tarit' and 'varun')
varun
print('tarit' and 'varun')
varun
print('tarit and varun')
tarit and varun
fav=list()
print(fav)
[]
print(type(fav))
<class 'list'>
fruits=['mango','grapes','papaya','watermelon']
print(fruits)
['mango', 'grapes', 'papaya', 'watermelon']
print(type(fruits))
<class 'list'>

li=[10,20.0,2+3j,'prava',[],{'sam',10,True},False]
li
[10, 20.0, (2+3j), 'prava', [], {True, 'sam', 10}, False]
fruits=('mango','grapes','papaya','watermelon')print(fruits)
SyntaxError: invalid syntax
fruits=('mango','grapes','papaya','watermelon')
print(fruits)
('mango', 'grapes', 'papaya', 'watermelon')
print(type(fruits))
<class 'tuple'>
li1=[10,10,40,30,50,"prava","prava"]
li1
[10, 10, 40, 30, 50, 'prava', 'prava']
tu=(10,10,40,30,50,"prava","prava")
print(tu)
(10, 10, 40, 30, 50, 'prava', 'prava')
tu1=(10,20.0,2+3j,'prava',[],{'sam',10,True},False)
print(tu1)
(10, 20.0, (2+3j), 'prava', [], {True, 'sam', 10}, False)
l=[10,30,40,50]
l
[10, 30, 40, 50]
l[0]=20
l
[20, 30, 40, 50]
t=(10,30,40,50)
t
(10, 30, 40, 50)
type(t)
<class 'tuple'>
t[0]=20
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t[0]=20
TypeError: 'tuple' object does not support item assignment
l.append=60
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    l.append=60
AttributeError: 'list' object attribute 'append' is read-only
l.append(60)
l
[20, 30, 40, 50, 60]
t
(10, 30, 40, 50)
t.append(80)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t.append(80)
AttributeError: 'tuple' object has no attribute 'append'
tu=()
print(tu)
()
print(type(tu))
<class 'tuple'>
tu=tuple()
tu
()
print(type(tu))
<class 'tuple'>
fruits={'mango','grapes','papaya','watermelon'}
fruits
{'mango', 'grapes', 'papaya', 'watermelon'}
fruits
{'mango', 'grapes', 'papaya', 'watermelon'}
num={10,20,30,40}
num
{40, 10, 20, 30}
fruits
{'mango', 'grapes', 'papaya', 'watermelon'}
fruits
{'mango', 'grapes', 'papaya', 'watermelon'}
num
{40, 10, 20, 30}
num
{40, 10, 20, 30}
num={10,20,30,40,10,10,30,50,60}
num
{50, 20, 40, 10, 60, 30}
num
{50, 20, 40, 10, 60, 30}
num
{50, 20, 40, 10, 60, 30}
num={50, 20, 40, 10, 60, 30}
num[0]=40
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    num[0]=40
TypeError: 'set' object does not support item assignment
num.append("prava")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    num.append("prava")
AttributeError: 'set' object has no attribute 'append'
num.add("prava")
num
{50, 20, 40, 10, 60, 30, 'prava'}
num[0]="sam"
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    num[0]="sam"
TypeError: 'set' object does not support item assignment
li=[10,20.0,2+3j,'prava',[],{'sam',10,True},False,{101:'hima',102:'prava'}]
li
[10, 20.0, (2+3j), 'prava', [], {True, 'sam', 10}, False, {101: 'hima', 102: 'prava'}]
d={1:"prava",2:"Anu",3:"santhu",4:"teju"}
d
{1: 'prava', 2: 'Anu', 3: 'santhu', 4: 'teju'}
print(type(d))
<class 'dict'>
d[1]
'prava'
print(d[2])
Anu
print(d['santhu'])
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    print(d['santhu'])
KeyError: 'santhu'
d={1:"prava",2:"Anu",3:"santhu",4:"teju",5:"Prava",6:"anu"}
d
{1: 'prava', 2: 'Anu', 3: 'santhu', 4: 'teju', 5: 'Prava', 6: 'anu'}
print(d[2])
Anu
print(d[6])
anu
print(d[5])
Prava
s={}
s
{}
type(s)
<class 'dict'>
s=dict()
s
{}
type(s)
<class 'dict'>
s=set()
s
set()
type(s)
<class 'set'>
s=frozenset{1,2,3,4}
SyntaxError: invalid syntax
s=frozenset({1,2,3,4})
s
frozenset({1, 2, 3, 4})
s=frozenset()
s
frozenset()
type(s)
<class 'frozenset'>
s=frozenset({1,2,3,4,4,3,5,1})
s
frozenset({1, 2, 3, 4, 5})
s
frozenset({1, 2, 3, 4, 5})
s
frozenset({1, 2, 3, 4, 5})
s=frozenset({1,2,3,4,4,3,5,1,"prava",True})
s
frozenset({1, 2, 3, 4, 5, 'prava'})
s
frozenset({1, 2, 3, 4, 5, 'prava'})
