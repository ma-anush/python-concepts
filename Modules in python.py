import random  # import a random module it is used to generate random numbers and performs random selection

# types
# 1. random()------ it is returns as a random float between o.0 and 1.0

a= random.random()
print (a) #0.5930140894092256

# 2. Randit()---- its returns a random integer 
a =random.randint(1,10)
print(a) # 6

# 3. uniform()----- returns a random float specify a number between a random float
b=random.uniform(1,10)
print(b) #7.450748852514938

# 4. Choice()------ Returns a random element from a non-empty  sequence--> can be a list, tuple , set
num =[1,2,3,4,5,6,7,8,9,33,4,55]
c= random.choice(num)
print(c) # randomly it provide a choice 

# 5 Shuffle()----- Shuffle the sequence in place
l1 =[1,2,3,4,5,6,7,8,9,10]
random.shuffle(l1)
print(l1) # it will be a shuffle a given sequence 

# 6 Sample() ---- select unique elements from the Population
t =["Anush","berlin","saktho","power"]
d = random.sample(t,1)
print(d)


# small random generate otp 


# Generate a 6-digit OTP


# Generate a 6-digit OTP
otp = random.randint(1000, 9999)
print("Your OTP is:", otp)

