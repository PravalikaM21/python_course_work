s=sorted([(1,3),(2,1),(4,2)]),key=lambda i:i[1]
print(s)

l=[(1,3,9),(2,1,7),(4,2,6)]
s=sorted(l,key=lambda i:i[-1])
print(s)

l=["Pravalika","shailu","Anu"]
s=sorted(l,key=lambda i:i[-1])
print(s)