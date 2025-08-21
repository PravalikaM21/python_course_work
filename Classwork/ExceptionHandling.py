try:
    a=10
    a=a+10
    l=[1,3,4]
    k=l[2]
    d={1:2,2:4,3:9}
    print(d[2])
    b=int(input("Enter a number:"))
    print(b)
    c=1+"1"
except NameError:
    print("a is not defined")
except IndexError:
    print("you have entered the out of range value")
except KeyError:
    print("Key is not present")
except ValueError:
    print("Enter the proper datatype")
except TypeError:
    print("You cant add 2 diff types")