'''num=int(input())
if num % 3 ==0:
  if num>5:
    print("yes")
  else:
    print("no")
else:
  print("no")
#----------------------------------------
num=int(input())
if num % 3 ==0 and num > 5:
    print("yes")
else:
  print("no")
#----------------------------------------
num=int(input())
if num >0:
    if num%2 == 0:
        print("yes")
    else:
        print("no")
else:
    print("no")
#output: 10
        #yes
        #7
        #no
#----------------------------------------
num=int(input())
if num >0:
    if num%2 == 0:
        print("yes")
    else:
        print("no")
else:
    print("no")
#output: 10
        #yes
        #7
        #no
#-------------------------------------------------
lst=[2,3]
lst.insert(1,1)
print(lst) #[2, 1, 3]

lst=[1,3]
lst.insert(0,2)
print(lst) #[2, 1, 3]

l=[7,8]
l.append(9)
print(l)

print(l.append(9))

print([7,8].append(9))
#--------------------------------------------------------
x = 5

if x > 0:
    if x > 10:
        print('Big')
    elif x == 5:
        print('Five')
    else:
        print('Neg')
#output:Five
#-------------------------------------------------------------
x = 5
if x > 0:
  pass'''
#--------------------------------------------------------------
n = int(input('enter a number'))
if n < 10:
    if n % 2 != 0:
        print("small")
    else:
        print("big")
else:
    print("10 or more")
