'''s=sorted([(1,3),(2,1),(4,2)]),key=lambda i:i[1]
print(s)

l=[(1,3,9),(2,1,7),(4,2,6)]
s=sorted(l,key=lambda i:i[-1])
print(s)

l=["Pravalika","shailu","Anu"]
s=sorted(l,key=lambda i:i[-1])
print(s)

data={'tarit':90,'prava':98,'dharani':80,'shivani':67}
sorted_data=sorted(data.items(),key=lambda i:i[1])
print(sorted_data)
print(sorted(data))
print(data.keys())
print(sorted(data.values()))

list={1:3,2:1,4:2}
sorted_list=sorted(list.items(),key=lambda i: i[1])
print(sorted_list)

l=[1,2,3,4,5,6,7,8,9]
even=list(map(lambda l:l+2).split())
print(even)

l=(lambda i:len(i))("python")
print(l)

name="python"
l=(lambda i:len(i))(name)
print(l)


#1) Square of a number 
square=lambda a:a*a
print(square(10))
print(square(15))
print(square(14))

#2) Check if number is even 
even=lambda n: "True" if n%2==0 else "False" 
print(even(9))
print(even(10))
print(even(30))

# 3)Fine maximum of two numbers
maxno=lambda a,b : a if a>b else b
print(maxno(9,30))
print(maxno(40,30))
print(maxno(13,12))

#4) Multiply two numbers
mulno=lambda a,b:a*b
print(mulno(2,3))
print(mulno(5,3))
print(mulno(6,8))
'''
#5) Sort list of tuple by second element
l=[(1,3),(2,1),(4,2)]
data=sorted((l,key=lambda i:i[1]))
print(data)