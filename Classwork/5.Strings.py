#5.Strings.py
#string is a group/set/collection of characters.
#string is immutable.
name='pravalika'
print(name) #output:pravalika
name="pravalika"
print(name) #output:pravalika
name='''pravalika'''
print(name) #output:pravalika
print(type(name)) #output:<class 'str'>
print(len(name)) #output:9

#Operations on string
#1)concatenation(+)
str1= "uday"
str2= "kiran"
print(str1+str2) #udaykiran
print(str1+" "+str2) #uday kiran
str3= str1+str2
print(str1) #uday
print(str2) #kiran
print(str3) #udaykiran
#2)Repetition(*)
print(str1) #uday
print(str1*10) #udayudayudayudayudayudayudayudayudayuday
print("uday "  * 10) #uday uday uday uday uday uday uday uday uday uday
s="50"
print(s*10) #output:50505050505050505050
#3.Indexing
text="python"
print(text[0]) #P
print(text[2]) #t
print(text[-1]) #n
print(text[-3]) #h
#4.Slicing([start:end:step])
names="PravalikaMounikaSravaniUdayKiran"
#i)Positive slicing:
print(names) #PravalikaMounikaSravaniUdayKiran
print(len(names)) #32
print(names[::]) #PravalikaMounikaSravaniUdayKiran
print(names[0:9]) #Pravalika
print(names[:9]) #Pravalika
print(names[9:16]) #Mounika
print(names[16:23]) #Sravani
print(names[23:32]) #UdayKiran
print(names[0::2]) #PaaiaonkSaaidyia(odd characters)
print(names[1::2]) #rvlkMuiarvnUaKrn(even characters)
#ii)Negative Slicing:
print(names[-1:]) #n
print(names[-1:-6:-1]) #nariK 
print(names[-6:-10:-1]) #yadU
print(names[-10:-17:-1]) #inavarS
print(names[-17:-24:-1]) #akinuoM
print(names[-24:-33:-1]) #akilavarP
print(names[::-1]) #nariKyadUinavarSakinuoMakilavarP
print(names[-1::-1]) #nariKyadUinavarSakinuoMakilavarP
print(names[-1:-33:-1]) #nariKyadUinavarSakinuoMakilavarP
#5.Membership:
print(text) #python
print("t" in text) #True
print("on" in text) #True
print("python" in text) #True
print("program" in text) #False
print("program" not in text) #True
print("python" not in text) #False
print("Pravalika" not in names) #False
print("Hema" not in names) #True

#Built_In_String Functions in string
#(len(),min(),max(),char(),ord())
print(names) #PravalikaMounikaSravaniUdayKiran
print(len(names)) #32
print(min(names)) #K
print(max(names)) #y
print(chr(60)) #<
print(ord("A")) #65
print(ord("a")) #97

#String Methods:
lname="muchanthala"
fullname="pravalika muchanthala"
print(lname.upper()) #MUCHANTHALA
print(lname.lower()) #muchanthala
print(fullname.capitalize()) #Pravalika muchanthala
print(fullname.title()) #Pravalika Muchanthala
print(lname.casefold()) #muchanthala
print(lname.swapcase()) #MUCHANTHALA

#Alignment & Formatting Methods:
print("python".center(10, "*")) #"*python*"
print("py".ljust(5, "-")) # "py---"
print("py".rjust(5, "-")) # "---py"
print("560".zfill(5)) # "000560"







