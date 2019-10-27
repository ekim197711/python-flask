
class Alien:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "age {}, name {}, greeting {}".format(self.age, self.name, self.greeting)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newvalue):
        self.__age = newvalue
        self.greeting = "Hello I come in peace...\n My name is {} and Im {} years old".format(
            self.name, self.age)

alien = Alien("LargeAndSlimy", 2500)
alien.age = alien.age + 1
print(alien)

