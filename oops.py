# how to create a class
class anush:
    color="maroon"
    num_rooms=4
    num_kitchens=1

#how to acess a from using object ((in here berlin is a object))
berlin = anush()
print(berlin.color)

#Constructor (__init__) it is a constructor 
# when the object is created the construcyor will automatically work
class tommy:
    def __init__(self,color,brand):
        self.color= color
        self.brand = brand
pet = tommy("brown","shephard")
print(pet.color)
print(pet.brand)

#----------------------- it is a workflow of a constructor


# Inheritance
#-- allows one class to get methods and arrtibutes from another class
# EG 1
class Animal:
    def sound(self):
        print("animals makes a sound")
class Dog(Animal):
    def bark(self):
        print("the dogs are barking")
bigdog =Dog() # this is a ex of how the child calss will acess the parent behviour
bigdog.sound()

