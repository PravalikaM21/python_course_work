#Keywords:
import keyword
print(keyword.kwlist) #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
#'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Tokens:
a=10
b=20
if a > b:
    print("a is greater")
else:
    print("a is smaller ")
'''a - identifier
= -operator
10 - literal
b - identifier
20 - literal
if - keyword
> - operator
: - punctuation
print() -identifier
"a is greater" - literal
else -keyword '''