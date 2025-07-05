#5.Strings.py
#string is a group/set/collection of characters.
#string is immutable.
name='pravalika'
print(name) #output:pravalika
name="pravalika"
print(name) #output:pravalika
name=''pravalika''
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
print(chr(60)) #7

#String Methods:
#1)Case Conversion Methods:
lname="muchanthala"
fullname="pravalika muchanthala"
print(lname.upper()) #MUCHANTHALA
print(lname.lower()) #muchanthala
print(fullname.capitalize()) #Pravalika muchanthala
print(fullname.title()) #Pravalika Muchanthala
print(lname.casefold()) #muchanthala
print(lname.swapcase()) #MUCHANTHALA

#2)Alignment & Formatting Methods:
print("python".center(10, "*")) #"*python*"
print("py".ljust(5, "-")) # "py---"
print("py".rjust(5, "-")) # "---py"
print("560".zfill(5)) # "000560"
s="python programming"
print(s) #python programming
print(s .center(60, '-')) #---------------------python programming---------------------
print(s.ljust(60,'-')) #python programming------------------------------------------
print(s.rjust(60,'-')) #------------------------------------------python programming
print(s.zfill(40)) #0000000000000000000000python programming

#3)Search & Find Methods:
print(text) #python
print(text.find("p")) #0
print(text.find("m")) #-1(if valuue not found it returns -1 as output)
print(s.rfind("g")) #17
print(s.rfind("p")) #7
print(text.index("p")) #0
print(text.index("n")) #5
print(text.index("y")) #1
print("hello".rindex("e")) #1
print("hello".rindex("l")) #3
#print("hello".rindex("y")) #ValueError: substring not found(if valuue not found raise an error)
print(text.count("p")) #1
print(s.count("p")) #2
print("hello".count("p")) #0
print("banana".count("na")) #2
print("abcbcbc".count("cbc")) #1

#4) String Testing Methods (Boolean Results):
c="DataScience"
print(c.startswith("D")) #True
print(c.endswith("e")) #True
print("prava123".isalnum() ) #True
print("rakshitha".islower()) # True
print("SUNIL".isupper())  #True
print("prava lika".isspace()) #False
print(" ".isspace()) #True
print("Dharani Duvasi".istitle() ) #True
print("num1".isidentifier()) #True 
print("23".isdecimal()) #True
print("10".isdigit()) #True
print("10".isnumeric()) #True
li=["sample.py","data.txt","student.xls","practice.py"]

#5. Replace & Modify Methods:
print("mounika".replace("ika","neha")) #mounneha
print("mouna".replace("a","i")) #mouni
print("udaykiran".translate(str.maketrans("ay","pa"))) #udpakirpn
print("abcdcde".translate(str.maketrans("cd","ud"))) #abudude
print("python".maketrans("pon","bca")) #{112: 98, 111: 99, 110: 97}
print(ord("p")) #112

#6. Splitting & Joining Methods:
print("prava,uday,sravs".split(",")) #['prava', 'uday', 'sravs']
print("prava,uday,sravs".rsplit(",")) #['prava', 'uday', 'sravs']
print("prava,uday,sravs".splitlines(",")) #['prava,uday,sravs']
print("prava,uday,sravs".partition(",")) #('prava', ',', 'uday,sravs')
print("prava,uday,sravs".rpartition(",")) #('prava,uday', ',', 'sravs')

#7. Whitespace & Trimming Methods:
print("data science ".strip()) #data science
print("----datascience".lstrip("-")) #datascience
print("datascience---- ".rstrip("-")) #datascience----

#8. Encoding & Decoding Methods:
text="java30💯"
print("java30💯".encode()) #b'java30\xf0\x9f\x92\xaf'
print(b'java30\xf0\x9f\x92\xaf'.decode()) #java30💯
text1 = "Hello 🌈"
print(text1.encode()) #b'Hello \xf0\x9f\x8c\x88'
print(b'Hello \xf0\x9f\x99\x82'.decode()) #'Hello 🌈'
print("welcome".encode()) #b'welcome'
print(b"welcome".decode()) #welcome