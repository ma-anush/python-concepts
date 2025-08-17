# set data structure
# creating a set 
s1 = {"anush","berlin","power"}
print(type(s1))

# creating a set using set function()
a = set(range(1,14,2))
print(a)
print(type(a))

# Imp functions preent in set()

s2 ={"anush",True,"berlin","sakthi","power"}
print(s2)
s2.add(40) # adding in to a set
s3= s2.copy()
print( (id), s2)
s2.remove("anush")
print(s2)

print(s2)
# clear() it will clear all the set it looks like a empty set


# mathamatical operations performed in list

s4 = {"anush","berlin","sakthi","muthu"}
s5 = {"kanyakumari","rajastam","muthu","karaikudi"}
s7= s4 & s5 # intersection
s6 = s4 | s5 # Union
s8 = s4 ^ s5 # symmetric difference
s9 = s4 - s5
print(s6)
print(s7)
print(s8)
print(s9)

# using Membership operator in set

s10 =set(range(1,7))
print( 3 in s10)
print( 9 in s10)


# creating set comprehension 

s11 = {i for i in range(1,10) if i%2 == 0  }
print(s11)

# indexing and slicing was not present in set
# if you do means error will occur

# write a program to remove duplicates values in list 
#approach 1 = coverting list in to set

s11 = [1,2,6,8,6,4,2,1,4,9,8,6,5,]
s12 =set(s11)
print(s12)

# approach 2 using member ship operator
s13 = [1,2,6,8,6,4,2,1,4,9,8,6,5,]
s14 =[]
for i in s13:
    if i  not in s14:
        s14.append(i)
print(s14)