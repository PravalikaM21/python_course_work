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
'''

l=(lambda i:len(i))("python")
print(l)

name="python"
l=(lambda i:len(i))(name)
print(l)