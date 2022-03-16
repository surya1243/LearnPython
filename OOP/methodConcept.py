class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.__name = name #private attribute
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.__name, song)

    def dance(self):
        return "{} is now dancing".format(self.__name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())