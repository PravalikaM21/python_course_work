import re
res=re.match(r'HELLO','HELLO WORLD')
res=re.search(r'[0-9]{2}','ds-14-15')
res=re.findall(r'PFS','PFS-30-PFS-31-DS-14_15')# find all the values int he string
res=re.finditer(r'[0-9]','PFS-30-PFS-31-DS-14_15')#find the position of the value
res=re.fullmatch(r'^[6-9]/d{9}','937497498')
res=re.fullmatch(r'DS-..','DS-15')
res=re.findall(r'H..','Hot Hat Hit Hii')
res=re.findall(r'H.t','Hot Hat Hit Hii')
res=re.findall(r'/s','python pythno pyxhon')
res=re.split(r'[,]','python, c, c++, java')
res=re.split(r'[,;"]','python, c; c++" java')
res=re.sub(r'[aeiouAEIOU]','*',"Python Programming Language")# Replace the string with specific character
res=re.search(r'[0-9]','97hlo')
res=re.findall(r'\d{2}','78 56 38 39 38')
res=re.findall(r'\b\d{4}','78 5667 3878 39 38')
#print(res.group() if res else 'no pattern')
print(res)
#for i in res:
    #print(i.group(),i.start())