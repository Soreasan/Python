# Kenneth Adair

class Classroom:

    def __init__(self):
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def remove_person(self, person):
        self._people.remove(person)

    def greet(self):
        for person in self._people:
            person.say_hello()

class Person:

    #underscores mean we don't interact with this method, python does this when instantiating an object
    def __init__(self, name):
        #attribute of name
        self.name = name

    def say_hello(self):
        print(id(self))
        print("Hello, ", self.name)
room = Classroom()
room.add_person(Person("Scott"))
room.add_person(Person("Poonam"))
room.add_person(Person("Paul"))

room.greet()
