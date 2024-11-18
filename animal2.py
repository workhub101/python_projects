# Parent Class
class Animal:
    def __init__(self,name) -> None:
        self.name= name
    def eat(self):
        print(f"{self.name}is eating")
    def sleep(self):
        print(f"{self.name}is sleeping")

# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name
                 
                 }is barking")

my_dog = Dog("Buddy")
my_dog.bark()
my_dog.eat()
my_dog.sleep()