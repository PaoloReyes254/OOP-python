class dog():
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

toby = dog("Toby", 7)
print(toby.name)
print(toby.age)
toby.speak()
toby.change_age(10)
print(toby.age)
toby.add_weight(5)
print(toby.weight)
toby.add_fur_color("Light Brown")
print(toby.fur)

dog2 = dog("Tyson", 25)
dog2.speak()