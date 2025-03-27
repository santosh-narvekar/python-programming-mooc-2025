# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.combined_height = 0

    def add(self,person: Person):
        self.persons.append(person)
        self.combined_height += person.height

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False
    
    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.combined_height} cm")

        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_person = self.persons[0]
        for person in self.persons:
            if person.height <= shortest_person.height:
                shortest_person = person

        return shortest_person
    
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest_person = self.persons[0]
        for person in self.persons:
            if person.height <= shortest_person.height:
                shortest_person = person

        removed_person = ""
        for person in self.persons:
            if person.name == shortest_person.name:
                removed_person = person
                self.combined_height -= person.height
                self.persons.remove(person)

                break
        return removed_person
