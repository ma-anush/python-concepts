"""
a ={"name":"Anush","age":21,"name":"power"}

a["work"]="office"
print(a)
print(a["name"])
# dictionary is a mutable 
d2 ={"name":"Anush","age":21,"work":"office"}
d2["age"]=24
print(d2)
# another representation of dictionary 
d3={
    100:"orange",
    100:"chilli",# if having duplicates means it assign the output like latestwe entered element
    101:"apple",
    102:"mango",
    103:"berry"
}
print(d3)
d3[101]="graphe"
print(d3)

#   Deleting elements in dictionary 

del d3[101] #deleting a element using a key value
d3.clear() # clear means we clear the total dict in there {} braces only it show 
del d3 # it means total dictinary will delete if you bagain print anything means it show a error
#print(d3)

#print(d3[100])

# Important Functions in dictionary
d4 = dict(name="anush",age= 33, work="eating", village="rajasthan")
print(d4.keys()) # it will show the what re the keys present in a dict
print(d4.values()) # it will show the what are values present in dict
print(d4.popitem()) # it will pop the item what is having in the dict last element will pop
print(d4.pop("age")) # it will acess the key value that key refer and it will pop
print(d4.get("name")) # In dict key out of the box is you use the get() then output will be none
print(len(d4))
print(d4)
print(type(d4))

# items in dict
d5= dict(name= "anush",age= 21,work="writing",home="village")
print(d5.items())
for key,values in d5.items():
    print(f"{key} ===== {values}")


# copy() in dicionary
d6= dict(name= "anush",age= 21,work="writing",home="village")
print("\nd6 = ",d6,id(d6) )
d7 = d6.copy()
print("\nd7 =",d7,"\n",id(d7))

# set default in Dict
d8= dict(name= "anush",age= 21,work="writing",home="village")
print(d8.setdefault("name"))
print(d8.setdefault(100))
d9=d8.setdefault(300,"metre")
print(d8)

# update in Dict
d9 ={"name": "Anush", "age": 21}
d10={"work":"office","Village":"rome"}
d9.update(d10)
#d11 = d9+d10 #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(d9)

# dictionary comphrension

d11=range(10)
d12 ={i: i for i in d11 if i%2 == 0  }
print(d12)

d13 ={"apple","orange","mango"}
d14={i: len(d13) for i in d13 }
print(d14)


# mini application using Dictionary----------->>>>
a = range(1,10)
b= {i: i*i for i in a if i%2==0}
print(b)


d1 = {'a': 1}
d2 = {'b': 2}
combined = {**d1, **d2}
print(combined)

"""

D6= dict(name= "anush",age= 21,work="writing",home="village")
D8 = {i: i*i for i in range(1,21) if i %2 !=0  }
print(D8)
D7 ={20:"mango_juice"}
D6.update(D7)
print(D6.setdefault(100,"banana"))
print(D6["name"])
D6["age"]= 20
#del d6["work"]
print(D6.get("name"))
#print(d6.pop("age"))
#print(d6.popitem())
print(D6.keys())
print(D6.values())

print(D6)

s = "hello"
repeted=""
for char in s:
    repeted = char+repeted
print(repeted) 

# Reverse a string manually
string = "Hello"
reversed_str = ""

for char in string:
    reversed_str = char + reversed_str

print("Original String:", string)
print("Reversed String:", reversed_str)

n1 = 10 
a,b = 0,1
for _ in range(n1):
    print(a,end="")
    a,b=b, a+b



a=int(input("Enter value :" ))
b=int(input("Enter value : "))

print("Before swapping a :",a)
print("Before swapping b :",b)
#logic to swap without using third variable 
a=a+b 
b=a-b
a=a-b


print("After swapping a becomes :",a)
