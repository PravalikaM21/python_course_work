#Type Conversions.py
#integer:
a=10
print(a) #10
print(type(a)) #<class 'int'>
print(float(a)) #10.0
print(str(a))#'10'
print(complex(a)) # (10+0j)
print(bool(a))#True
#print(list(a)) #TypeError: 'int' object is not iterable
#print(tuple(a)) #TypeError: 'int' object is not iterable
#print(set(a)) #TypeError: 'int' object is not iterable
#print(dict(a)) #TypeError: 'int' object is not iterable

# Float:
b=20.2
print(b) #20.2
print(type(b)) #<class 'float'>
print(int(b)) #20
print(str(b)) #'20.2'
print(complex(b)) # (20.2+0j)
print(bool(b)) #True
#print(list(b)) #TypeError: 'float' object is not iterable
#print(tuple(a)) #TypeError: 'int' object is not iterable
#print(set(b)) #TypeError: 'float' object is not iterable
#print(dict(b)) #TypeError: 'float' object is not iterable

#Complex:
i=(2+3j)
print(i) # (2+3j)
print(type(i)) #<class 'complex'>
#print(int(i)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(str(i)) #(2+3j)
#print(float(i)) #TypeError: float() argument must be a string or a real number, not 'complex'
#print(list(i)) #TypeError: 'complex' object is not iterable
#print(set(i)) #TypeError: 'complex' object is not iterable
#print(list(i)) #TypeError: 'complex' object is not iterable
#print(dict(i)) #TypeError: 'complex' object is not iterable

# string:
c="pravalika"
print(c) # pravalika
print(type(c)) # <class 'str'>
print(int("10")) # 10
#print(int("10.0")) # ValueError: invalid literal for int() with base 10: 'pravalika'
#print(int(c)) # ValueError: invalid literal for int() with base 10: 'pravalika'
#print(float(c)) # ValueError: could not convert string to float: 'pravalika'
print(float("10")) # 10.0
print(float("10.0")) # 10.0
#print(complex(c)) # ValueError: complex() arg is a malformed string
print(bool(c)) # True
print(list(c)) # ['p', 'r', 'a', 'v', 'a', 'l', 'i', 'k', 'a']
print(tuple(c)) # ('p', 'r', 'a', 'v', 'a', 'l', 'i', 'k', 'a')
print(set(c)) #{'k', 'p', 'r', 'v', 'l', 'a', 'i'}
#print(dict(c)) #ValueError: dictionary update sequence element #0 has length 1; 2 is required

# List:
l = [1,2,3,4,5]
print(l) # [1, 2, 3, 4, 5]
print(type(l)) # <class 'list'>
#print(int(l)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(float(l)) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
print(str(l)) # [1, 2, 3, 4, 5]
print(bool(l)) # True
#print(complex(l)) # TypeError: complex() first argument must be a string or a number, not 'list'
print(tuple(l)) # (1, 2, 3, 4, 5)
print(set(l)) # {1, 2, 3, 4, 5}
#print(dict(l)) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
l1=[(1,2,3),(4,5,6),(8,9,10)]
#print(dict(l1)) #ValueError: dictionary update sequence element #0 has length 3; 2 is required
l2=[(1,2),(4,5),(8,9)]
#print(dict(l2)) #{1: 2, 4: 5, 8: 9}