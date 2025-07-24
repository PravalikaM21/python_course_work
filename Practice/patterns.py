'''for rows in range(4):
    for col in range(4):
        print(col,end=" ")
    print()

for rows in range(4):
    for col in range(4):
        print(rows+1,end=" ")
    print()'''

for rows in range(5):
    for col in range(rows-1):
        print("",end=" ")
    for s in range(rows+1):
        print(rows,end=" ")
    print()

