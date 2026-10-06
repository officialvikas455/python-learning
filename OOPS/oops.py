# class Car:
#     a = 2 #atttribute
#     def hello(): #method
#         print("hello")

# print(Car.a) # accessing attributes
# Car.hello()  # accessing methods

# class Bags:
#     name = "gangwar"

#     def details(self):
#         print("This is your company which creates bag")

# reebok = Bags()

# print(reebok.name)

# reebok.details()


# class Bags:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

# le = Bags("leather", 3, 2)


# class Animal:
#     a = 12

#     def __init__(self,name):
#         self.name = name  #instance attribute

#     def hello(self):
#         print("how are you")

#     @classmethod
#     def details(cls): #captures the location of the class
#         print(f"How are you my name is {cls.a}")


#     @staticmethod
#     def speak(): # this the static method this is not target the value
#         print("Hello I am the static method")



# obj = Animal("lion")

# obj.details()


# INHERITANCE
# class Animal: # parent class
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print("Your name is self name")

# class Humans(Animal):  #child class
#     pass

# obj = Animal("Lion")
# obj2 = Humans("Vikas")
# obj2.details()

# print(obj2.name)


# class BagFactory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def details(self):
#         print("Your bag details are avaiable")
#         print(self.material)
#         print(self.email)
#         print(self.zips)


# class Reebok(BagFactory):
#     def __init__(self, material, zips, pockets,color):
#         super().__init__(material, zips, pockets)
#         self.color = color

#         def details(self):
#             print(self.color)
#             return super.details()

# class Campus(Reebok):
#     def __init__(self, material, zips, pockets, color): # multilevel Inheriatance
#         super().__init__(material, zips, pockets, color)


# bag1 = BagFactory("Leather",3,4)
# bag2 = Reebok("Ployster",4,5)



# # Multiple inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Humans:
#     def __init__(self, id):
#         self.id = id

# class Robots(Humans, Animal):
#     def __init__(self, id, name):
#         Humans.__init__(id)
#         Animal.__init__(name)
# robo = Robots(12,"Vikas")



#Polymorphism


# class Animal:
#     def Speak(self):
#         print("Animals will not speak")

# class Humans:
#     def Speak(self):
#         print("We are humans we can speak")

# obj = Animal()
# obj2 = Humans()

# obj.Speak()
# obj2.Speak()


#method overriding(we need inheritance)

# class Animal:
#     a = 12
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print(f"your name is {self.name}");


# class humans(Animal):
#     b = 12
#     def __init__(self, name):
#         super().__init__(name)

#     def details(self):
#         print(f"info is {self.name}")

# obj = humans("Akash")
# obj.details()



#Encapsulation


# class Factory:
#     __name = "Kia" #public class attribute
#     def __init__(self,type,tyre, color):
#         self.color = color #public obj attribute
#         self.tyre = tyre
#         self.type = type

#     def details(self):
#         print("hello your details are :")



# obj = Factory("sedan","mrf", "black")
# obj.details()
# print(obj.__name)


# class hello:
#     __a = 12
#     @classmethod
#     def hello(cls):
#         print(cls.__a)

# obj = hello()


# abstraction

# from abc import ABC, abstractmethod

# from Python.OOPS.a import a

# class enforce(ABC):
#     @abstractmethod
#     def engineStart():
#         pass

# class bike(enforce):
#     def engineStart():
#         pass

# class car(enforce):
#     def engineStart():
#         pass

# class truck:
#     pass

# obj = bike()
# obj1 = car()
# obj2 = truck()



# dunder method

# class Animal:
#     def __init__(self,name):
#         self.name = name


#     def __str__(self):
#         return f"hello my name is {self.name}"

# obj = Animal("Lion")
# print(obj)


# class numbers:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self, other):
#        return self.num + other.num

#     def __eq__(self, value):
#         return self.num == value.num

# a = numbers(50)
# b = numbers(50)
# print(a + b)
# print(a==b)


# def extraGreeting(func):
#     def wrapper():
#         print("Hello I am Vikas Gangwar")
#         func
#         print("Thankyou for given me this opportunity")

#     return wrapper

# @extraGreeting
# def greeting():
#     print("Good Morning")

# greeting()


# args
# def addition(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s
# print(addition(3,4,4,9,9,9))


# kwargs


# def extraGreeting(func):
#     def wrapper(*args,**kwargs):
#         print("Hello I am Vikas Gangwar")
#         func(*args,**kwargs)
#         print("Thankyou for given me this opportunity")

#     return wrapper

# @extraGreeting
# def addition(a,b,c):
#     print( a + b + c)

# addition(1,3,4,6)
# a = 3
# print("even") if a % 2 == 0 else print("odd") #ternaly operation


# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# b = [i for i in a if i % 2==0]
# print(b)

# for i in  a:
#     if i % 2 == 0:
#         b.append(i)
#         print(b)

# addition = lambda *args : args + args
# print(addition(2,3))

#zip
name = ['vikas','gangwar']
marks = [12, 90]
result = list(zip(name, marks))
print(result)
