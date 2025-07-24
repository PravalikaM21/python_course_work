'''n=int(input("enter size"))
for row in range(n):
    if row<=n//2:
        print("*" * (row+1),end=" ")
    else:
        print("*" * (n-row),end=" ")
    print()

n=int(input("enter size"))
for i in range(4):
    for j in range(3):
        print("*",end=" ")
    print()
    
n=int(input("enter size"))
for i in range(4):
    for j in range(2):
        print("*",end=" ")
    print()

n=int(input("enter size"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=int(input("enter size"))
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
    
n=int(input("enter size"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

n=int(input("enter size"))
for i in range(n):
    for j in range(n):
        print(i+1,end=" ")
    print()

n=int(input("enter size"))
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()
    
n=int(input("enter size"))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()

n=int(input("enter size"))
for row in range(n):
    for col in range(row+1):
        print(row,end=" ")
    print()
    
11)n=int(input("enter size"))
for row in range(n):
    for col in range(n-row):
        print(" ",end=" ")
    for s in range(row+1):
        print("*",end=" ")
    print()
    
#14)
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#16)
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row== n//2 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#19)
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#20)
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#21)S
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or (col==0 and row<=n//2) or (row>=n//2 and col==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#22)A
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n//2 or col==0 or col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#24)P
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2 or (col==n-1 and row<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#25)L
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#26)E
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col==0 or row==0 or row==n//2 or row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#18)X
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col==row or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#17)Z

n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#12)
n=int(input("enter size"))
for row in range(n):
    for col in range(row+1):
        print(" ",end=" ")
    for s in range(n-row):
        print("*",end=" ")
    print()
#13)
n=int(input("enter size"))
for row in range(n):
    if row<=n//2:
        print("*" * (row+1),end=" ")
    else:
        print("*" * (n-row),end=" ")
    print()

#14) 0 1 0 1
n=int(input("enter size"))
for row in range(n):
    for col in range(n):
        if col%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()'''
#15) 0 1 0 1 and 1 0 1 0
rows = 4
cols = 4
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()




