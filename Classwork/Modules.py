# Modules.py
#import operator
import operator as opr
#from operators import *
#from operators import add,sub,mul,div

a=int(input("enter a value"))
b=int(input("enter b value"))
op =input("Enter operator(+,-,/,*,%)")
if op=='+' :
    opr.add(a,b)
elif op=='-':
    opr.sub(a,b)
elif op=='*':
    opr.mul(a,b)
elif op=='/':
    opr.div(a,b)
elif op=='%':
    opr.mod(a,b)

    