"""
# tuples 
t1 = "anush","power", "berlin"
print(type(t1))

#empty tuple

t2 =()
print(t2)
print(type(t2))

#tuple packing 
t3 = "anush","power", "berlin","muthu"
print(t3)

# Tuple Unpacking
t4 = (10,70,60)
a,b, c = t4
print(a)
print(b)
# create  tuple using range ()
t5 = tuple(range(1,9,2))
print(t5)

#assesing tuple elements using index
t6 =(10,6,9,7, True, False,"Anush")
print(t6[4])
print(t6[6])
#print(t6[8]) #IndexError: tuple index out of range


# acessing tuple elements using slice operater

t7= ("csk","mumbai","rajastan","punjab","uttar pradhesh","odukol","kanor")
print(max(t7))
print(min(t7))
print(t7)
t8 = sorted(t7)
print(t8)

print(t7[0:8:2])

# tuple comprehension 
# python doesnot support the tuple comprehension why means it compile but its run on a generoter operator 

t =(i for i in range(1,11) if i%2==0)
print(t)  #<generator object <genexpr> at 0x000002180AF136B0>

# applying concadination operator in tuple 

t9 =("csk","mumbai","rajastan","punjab")
t10 =(10,6,9,7)
t11=t9+t10
print(t11)

t12 = ("csk","mumbai","rajastan","punjab")
print(t12 * 4)

# covert a list into tuple

t13 = ["csk","mumbai","rajastan","punjab"]
print(tuple(t13))

# coverting tuplee in to list

t14 = ("csk","mumbai","rajastan","punjab")
print(list(t14))

j = (1,2,3)
h =(4,5,6)
n =j+h
print(n)
"""
string =("peter and potter went to waterfalls potter was about fall. butl"
"er saved him and served butter ")
s = list(string.split())
t =[]
print(s)
for i in s:
    if "t"and "e" and "r"in i:
        if i not in t:
            t.append(i)
print(t)