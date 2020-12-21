class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi there, I am a dog and I can talk, my name is " + self.name + " and I am " + str(self.age) + " years old")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

    def add_fur_color(self, fur):
        self.fur = fur

    def talk(self):
        print("Bark!")

class Cat(Dog):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
    
    def speak(self):
        print("Hi there, I am a cat and I can talk, my name is " + self.name + ", I am " + str(self.age) + " years old and I am " + self.size)

    def talk(self):
        print("Meow!")
        
dog1 = Dog("Toby", 7)
dog1.talk()
cat1 = Cat("Michi", 10, "small")
cat1.speak()
cat1.talk()