for row in range(5):
    for col in range(5):
        print("*",end=" ")
  
    print()
'''Output:
* * * * * 
* * * * *
* * * * * 
* * * * *
* * * * *
'''
for row in range(5):
    for col in range(5):
        print(col,end=" ")
    print()  
'''
output:
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''
for row in range(5):
    for col in range(5):
        print(row,end=" ")
    print()
'''
output:
0 0 0 0 0
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
'''
for row in range(5):
    for col in range(row+1):
        print(row,end=" ")
    print()
'''
output:
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    print()
'''
output:
*
* *
* * *
* * * *
* * * * * 
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print("*",end=" ")
    print()
'''
output:
* * * * * * * 
* * * * * *
* * * * *
* * * *
* * *
* *
* 
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for s in range(row+1):
        print("*",end=" ")
    print()
    '''
output:
              *    
            * *
          * * *
        * * * *
      * * * * *
    * * * * * *
  * * * * * * *
* * * * * * * * '''

rows = 5
for i in range(rows):
    print("  " * i, end="")  # Print leading spaces
    for j in range(rows - i):
        print("*", end=" ")    # Print stars
    print()  # Move to next line
'''
* * * * *
  * * * *
    * * *
      * *
        *'''

n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for s in range(row+1):
        print("*",end=" ")
    for spc in range(row):
        print(" ",end=" ")
    for col in range(n-row):
        print("*",end=" ")
    print()

for row in range(n):
        print(" "*row,end=" ")
        print("*"*(n-row),end=" ")
        print()       
'''
        *
      * *
    * * * 
  * * * * 
* * * * *
  * * * *
    * * *
      * *
        *
        '''