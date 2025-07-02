#3.Datatypes.py
#integer(int)
a=10 
print(a) #10
print(type(a))#<class 'int'>
#-------------------------------------------------------------------'''
#Float
a=10.0 
print(a) #10.0
print(type(a))#<class 'float'>
#-------------------------------------------------------------------'''
# Complex
a=3+3j
print(a) #3+3j
print(type(a)) #<class 'complex'>
#-------------------------------------------------------------------'''
#string
name="pravalika" #string with double quotes
print(name) #pravalika
print(type(name)) #<class 'str'>

name='pravalika' #string with single quotes
print(name) #pravalika
print(type(name)) #<class 'str'>

name='''pravalika''' #string with triple quotes
print(name) #pravalika
print(type(name)) #<class 'str'>
#-------------------------------------------------------------------------'''
#list
fav=[] #create / define an empty list
print(fav) #[]
fav=list() #create / define an empty list
print(fav) #[]
print("'tarit' and 'varun'") #'tarit' and 'varun'
print('tarit' and 'varun') #varun
print('tarit and varun') #tarit and varun
print(type(fav)) #<class 'list'>

fruits=['mango','grapes','papaya','watermelon']
print(fruits) #['mango', 'grapes', 'papaya', 'watermelon']
print(type(fruits)) #<class 'list'>

li=[10,20.0,2+3j,'prava',[],{'sam',10,True},False,(1,2,3,),{"name":"prava"}] #heterogenuos data(int,float,string,set,list,tuple,set,dict,Bool)
print(li) #[10, 20.0, (2+3j), 'prava', [], {True, 'sam', 10}, False,(1,2,3,),{"name":"prava"}]

li1=[10,10,40,30,50,"prava","prava"]
print(li1) #[10, 10, 40, 30, 50, 'prava', 'prava']

l=[10,30,40,50] #changing the value
print(l) #[10, 30, 40, 50]
l[0]=20
print(l) #[20, 30, 40, 50]
#-----------------------------------------------------------------------------------------'''
#Tuple
tu=() #create/define an empty tuple
print(tu) #()
print(type(tu)) #<class 'tuple'>

tu=tuple()  #create/define an empty tuple
print(tu) #()
print(type(tu)) #<class 'tuple'>

tu=(10,10,40,30,50,"prava","prava")
print(tu) #(10, 10, 40, 30, 50, 'prava', 'prava')
print(type(li)) #<class 'Tuple'>

tu1=(10,20.0,2+3j,'prava',[],{'sam',10,True},False,(1,2,3,),{"name":"prava"}) #heterogenuos data(int,float,string,set,list,tuple,set,dict,Bool)
print(tu1) #(10, 20.0, (2+3j), 'prava', [], {True, 'sam', 10}, False,(1,2,3,),{"name":"prava"})


t=(10,30,40,50)
print(t) #(10, 30, 40, 50)
print(type(t)) #<class 'tuple'>
#print(t[0]=20) #TypeError: 'tuple' object does not support item assignment
#t.append(80) #AttributeError: 'tuple' object has no attribute 'append'
#------------------------------------------------------------------------------'''
#Set
s=set()
print(s) #set()
print(type(s)) #<class 'set'>
# Note: we cant create an empty set with {}.
s={}
print(s) #{}
print(type(s)) #<class 'Dict'>

fruits={'mango','grapes','papaya','watermelon'}
print(fruits) #{'mango', 'grapes', 'papaya', 'watermelon'}

num={10,20,30,40}
print(num) #{40, 10, 20, 30}

num={10,20,30,40,10,10,30,50,60} #Duplicate data
print(num) #{50, 20, 40, 10, 60, 30}not allowed duplicates
num={50, 20, 40, 10, 60, 30}
#------------------------------------------------------------------------------'''
#Dictionary
s={} #create an empty dictionary
print(s) #{}
print(type(s)) #<class 'dict'>

s=dict() #create an empty dictionary
print(s) #{}
print(type(s)) #<class 'dict'>

d={1:"prava",2:"Anu",3:"santhu",4:"teju"}
print(d) #{1: 'prava', 2: 'Anu', 3: 'santhu', 4: 'teju'}
print(type(d)) #<class 'dict'>
print(d[1]) #'prava'
print(d[2]) #Anu
#print(d['santhu']) #KeyError: 'santhu'
      
d={1:"prava",2:"Anu",3:"santhu",4:"teju",5:"Prava",6:"anu"}
print(d) #{1: 'prava', 2: 'Anu', 3: 'santhu', 4: 'teju', 5: 'Prava', 6: 'anu'}
print(d[2]) #Anu
print(d[6]) #anu
print(d[5]) #Prava

#-------------------------------------------------------------------------'''
#Frozenset
s=frozenset=({1,2,3,4})
print(s) #frozenset({1, 2, 3, 4})

s=frozenset={1,2,3,4}
print(s) #SyntaxError: invalid syntax