'''
s="123455hjjriksljg"
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
    else:
        l.append(0)
print(l)
'''
s="123455hjjriksljg"
l=[]
l=[i if i.isdigit() else 0 for i in s]
print(l)
