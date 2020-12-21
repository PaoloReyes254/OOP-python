class Dog(object):
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(name)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @classmethod
    def dog_names(cls):
        for i in cls.dogs:
            print(i)
    
    @staticmethod
    def bark_times(n):
        for i in range(n):
            print("Bark!")

dog1 = Dog("Inge")
dog2 = Dog("Paolo")
dog3 = Dog("Mr Macnolo")
dog4 = Dog("Obed")

print(Dog.num_dogs(), "dogs")
Dog.dog_names()
Dog.bark_times(2)