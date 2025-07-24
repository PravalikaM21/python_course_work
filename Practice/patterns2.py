#I
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#H
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#4 small squares
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or col==n-1 or col==n//2 or col==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#or (col==n-1 or col==n//2)

#Letter E:
#-------------------------
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row==n//2 or col==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#letter L:
#----------------------------------
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#letter P:
#----------------------------------
n=int(input("Enter size:"))
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
