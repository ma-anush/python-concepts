# python to print Welcome Message
"""
def anush(a):
    print(f"{a}")
anush("Welcome Anush")
print()
"""
# No input no output Function
"""def anush():
    a=int(input("Enter a number :"))
    b = int(input("enter a number :"))
    c= a+b
    print(c)
anush()

# Input But No Output Function
def anusha(e,f):
    
    e=int(input("Enter a number :"))
    f= int(input("enter a number :"))
    sum = e+f
    return sum
result = anusha
print(anusha)

string =("peter and potter went to waterfalls potter was about fall. butter saved him and served butter ")
s = string.split()
t =set()

print(s)
for i in s:
    if "ter" in i:
        t.add(i)
f=list(t)
print(f)


b = [1,2,3,4,5,6,7,8,9,10]
l=list(filter(lambda a: a%2==0,b))
print(l)
"""

# Largest element in a list using if-else
# Reverse a list using loop
lst = [1, 2, 3, 4, 5]
rev = []

for item in lst:
    rev = [item]+ rev   # insert at front

print("Reversed list:", rev)

