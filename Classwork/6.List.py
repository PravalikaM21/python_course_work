#6 List.py
l=[1,2,3,4,5,6]
print(l) #[1, 2, 3, 4, 5, 6]
l1=[1,2,3,4,5,6,2,2,44,3,4]
print(l1) #[1, 2, 3, 4, 5, 6, 2, 2, 44, 3, 4]
print(l1[0]) #1
print(l1[4]) #5
print(l1[-1]) #4
print(l1[-5]) #2
print(l) #[1, 2, 3, 4, 5, 6]
l.append("prava")
print(l)
l.extend(["mouna",3,9.0,{3,4,5},(6,7),{101:'sai'},True])
print(l)
l2=["mouna",3,9.0,{3,4,5},(6,7),{101:'sai'},True]
print(l2) #['mouna', 3, 9.0, {3, 4, 5}, (6, 7), {101: 'sai'}, True]
print(l2[3]) #{3, 4, 5}
