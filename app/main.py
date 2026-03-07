class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    if people == []:
        return []
    people_class_list = []
    for person in people:
        people_class_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            people_class_list[i].wife = Person.people[people[i]["wife"]]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            people_class_list[i].husband = Person.people[people[i]["husband"]]
    return people_class_list
