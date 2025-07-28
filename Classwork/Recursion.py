# Recursion.py:
'''
->Recursion means calling a function itself is know as recrsion.
->Base condition
'''
#sum of numbers:
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
n=int(input("enter a number"))
print(sum(n))
'''Output:
enter a number5
15'''
# Product of numbers:
def product(n):
    if n==1:
        return 1
    else:
        return n*product(n-1)
n=int(input("Enter a number"))
print(product(n))
'''Output:
Enter a number5
120'''